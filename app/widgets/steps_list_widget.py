from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from app.core.constants import STEP_LIST_OBJECT_ROLE
from app.sections.step.step_store import StepEntity

PADDING = 5


class StepItemDelegate(QStyledItemDelegate):
    TITLE_FONT_SIZE = 12
    TITLE_FONT_BOLD = True
    DESCRIPTION_FONT_SIZE = 10
    DESCRIPTION_FONT_BOLD = False

    def sizeHint(self, option: QStyleOptionViewItem, model_index: QModelIndex):
        if not model_index.isValid():
            return

        bounding_rect = option.rect

        step_entity: StepEntity = model_index.data(STEP_LIST_OBJECT_ROLE)

        step_title = step_entity.title
        step_description = step_entity.description

        # title
        font: QFont = QApplication.font()
        font.setPointSize(self.TITLE_FONT_SIZE)
        font.setBold(self.TITLE_FONT_BOLD)
        font_metrics: QFontMetrics = QFontMetrics(font)
        title_rect = font_metrics.boundingRect(
            0, 0, bounding_rect.width(), 0, Qt.AlignLeft | Qt.AlignTop, step_title
        )

        # description
        font.setPointSize(self.DESCRIPTION_FONT_SIZE)
        font.setBold(self.DESCRIPTION_FONT_BOLD)
        font_metrics: QFontMetrics = QFontMetrics(font)
        description_rect = font_metrics.boundingRect(
            0, 0, bounding_rect.width(), 0, Qt.AlignLeft | Qt.AlignTop, step_description
        )
        size: QSize = QSize(
            option.rect.width(), title_rect.height() + description_rect.height() + 10 * PADDING
        )

        return size

    def paint(
            self, painter: QPainter, option: QStyleOptionViewItem, model_index: QModelIndex
    ):
        if not model_index.isValid():
            return

        bounding_rect = option.rect
        painter.save()

        step_entity: StepEntity = model_index.data(STEP_LIST_OBJECT_ROLE)

        step_title = step_entity.title
        step_description = step_entity.description

        font: QFont = QApplication.font()
        font.setPointSize(self.TITLE_FONT_SIZE)
        font.setBold(self.TITLE_FONT_BOLD)
        font_metrics: QFontMetrics = QFontMetrics(font)
        elided_title = font_metrics.elidedText(
            step_title, Qt.ElideRight, bounding_rect.width() - 10 * PADDING
        )
        # title
        title_rect = font_metrics.boundingRect(
            bounding_rect.left() + PADDING,
            bounding_rect.top() + PADDING,
            bounding_rect.width() - 10 * PADDING,
            0,
            Qt.AlignLeft | Qt.AlignTop,
            elided_title,
        )
        painter.drawText(
            title_rect, Qt.AlignLeft | Qt.AlignTop | Qt.TextWordWrap, elided_title
        )

        # description
        font.setPointSize(self.DESCRIPTION_FONT_SIZE)
        font.setBold(self.DESCRIPTION_FONT_BOLD)
        font_metrics: QFontMetrics = QFontMetrics(font)
        elided_description = font_metrics.elidedText(
            step_description, Qt.ElideMiddle, bounding_rect.width() - 5 * PADDING
        )

        description_rect = font_metrics.boundingRect(
            title_rect.left(),
            title_rect.bottom() + 2 * PADDING,
            bounding_rect.width() - PADDING,
            0,
            Qt.AlignLeft | Qt.AlignTop,
            elided_description,
        )
        painter.drawText(
            description_rect, Qt.AlignLeft | Qt.AlignTop | Qt.TextWordWrap, elided_description
        )

        painter.restore()


class CustomStepsListView(QListView):
    drop_event_signal = pyqtSignal(QModelIndex)

    def __init__(self, parent=None):
        super().__init__(parent)

    def dropEvent(self, e: QDropEvent):
        super().dropEvent(e)
        model_index = self.indexAt(e.pos())
        self.drop_event_signal.emit(model_index)
