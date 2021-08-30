import logging
from queue import Queue
from typing import Any

import attr

from app.commands.run_step_command import RunStepCommand
from app.scheduling.worker_thread import WorkerThread


@attr.s(auto_attribs=True)
class WrappedRunStepCommand(object):
    run_step_command: RunStepCommand
    on_success: Any
    on_failure: Any


class WorkerPool:
    def __init__(self, world):
        self.world = world
        self.worker_queue: Queue = Queue()
        self.any_worker_running: bool = False
        self.current_worker = None

    def schedule(self, run_step_command):
        logging.info("Schedule Step command: {}".format(run_step_command))
        wrapped_command = WrappedRunStepCommand(
            run_step_command=run_step_command,
            on_success=self.on_success_after_command_run,
            on_failure=self.on_failure_after_command_run
        )
        self.worker_queue.put(wrapped_command)
        self.process_queue()
        logging.info("Worker Queue size: {}".format(self.worker_queue.qsize()))

    def process_queue(self):
        if self.any_worker_running:
            logging.info("Worker running. Will check again once it finished processing")
        elif not self.worker_queue.empty():
            wrapped_command = self.worker_queue.get()
            self.process_command(wrapped_command)
            self.any_worker_running = True
        else:
            logging.info("Nothing in the queue")

    def process_command(self, wrapped_command):
        logging.info("Sending wrapper command to Worker -> {}".format(wrapped_command))
        self.current_worker = WorkerThread(self.world, wrapped_command)
        self.current_worker.start()

    def on_success_after_command_run(self):
        pass

    def on_failure_after_command_run(self):
        pass
