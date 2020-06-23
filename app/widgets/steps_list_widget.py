from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from app.core.constants import STEP_LIST_OBJECT_ROLE
from app.sections.step.step_store import StepEntity
from app.themes.theme_provider import is_dark

PADDING = 5


def step_selected_rect():
    return QColor("#505153") if is_dark() else QColor("#CBD8E1")


def step_selected_pen():
    return Qt.white if is_dark() else Qt.black


def step_bounded_rect_pen():
    return Qt.white


def step_bounded_rect_fill():
    return QColor("#6ea0da")


def success_color():
    return QColor("#01721d") if is_dark() else QColor("#01721d")


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

        # title
        font: QFont = QApplication.font()
        font.setPointSize(self.TITLE_FONT_SIZE)
        font.setBold(self.TITLE_FONT_BOLD)
        font_metrics: QFontMetrics = QFontMetrics(font)
        title_rect = font_metrics.boundingRect(
            0, 0, bounding_rect.width(), 0, Qt.AlignLeft | Qt.AlignTop, step_title
        )

        size: QSize = QSize(
            option.rect.width(),
            title_rect.height() +
            10 * PADDING,
        )

        return size

    def paint(
            self, painter: QPainter, option: QStyleOptionViewItem, model_index: QModelIndex
    ):
        if not model_index.isValid():
            return

        bounding_rect = option.rect
        painter.save()

        if option.state & QStyle.State_Selected:
            painter.fillRect(bounding_rect, step_selected_rect())
            painter.setPen(step_selected_pen())

        step_entity: StepEntity = model_index.data(STEP_LIST_OBJECT_ROLE)

        step_title = step_entity.title
        step_description = step_entity.description
        step_type = step_entity.step_type.value
        padded_step_type = f"   {step_type}   "

        # start draw type

        font: QFont = QApplication.font()
        font.setPointSize(self.TITLE_FONT_SIZE)
        font_metrics: QFontMetrics = QFontMetrics(font)
        step_type_rect: QRect = font_metrics.boundingRect(
            bounding_rect.left() + PADDING,
            bounding_rect.top() + PADDING,
            0,
            0,
            Qt.AlignLeft | Qt.AlignTop,
            padded_step_type
        )
        painter.setRenderHint(QPainter.Antialiasing)
        path = QPainterPath()
        path.addRoundedRect(QRectF(step_type_rect), 2, 2)
        painter.fillPath(path, step_bounded_rect_fill())
        painter.setFont(font)
        painter.setPen(step_bounded_rect_pen())
        painter.drawText(
            step_type_rect, Qt.AlignLeft | Qt.AlignTop, padded_step_type
        )

        # end draw type

        # start draw title
        font: QFont = QApplication.font()
        font.setPointSize(self.TITLE_FONT_SIZE)
        font.setBold(self.TITLE_FONT_BOLD)
        font_metrics: QFontMetrics = QFontMetrics(font)
        elided_title = font_metrics.elidedText(
            step_title, Qt.ElideRight, bounding_rect.width() - 10 * PADDING
        )
        # title
        title_rect = font_metrics.boundingRect(
            step_type_rect.right() + PADDING,
            bounding_rect.top() + PADDING,
            bounding_rect.width() - 10 * PADDING,
            0,
            Qt.AlignLeft | Qt.AlignTop,
            elided_title,
        )
        painter.setFont(font)
        painter.setPen(step_selected_pen())
        painter.drawText(
            title_rect, Qt.AlignLeft | Qt.AlignTop | Qt.TextWordWrap, elided_title
        )
        # end draw title

        # start draw description

        font.setPointSize(self.DESCRIPTION_FONT_SIZE)
        font.setBold(self.DESCRIPTION_FONT_BOLD)
        font_metrics: QFontMetrics = QFontMetrics(font)
        elided_description = font_metrics.elidedText(
            step_description, Qt.ElideMiddle, bounding_rect.width() - 5 * PADDING
        )
        description_rect = font_metrics.boundingRect(
            step_type_rect.left(),
            step_type_rect.bottom() + 2 * PADDING,
            bounding_rect.width() - PADDING,
            0,
            Qt.AlignLeft | Qt.AlignTop,
            elided_description,
        )
        painter.setFont(font)
        painter.setPen(step_selected_pen())
        painter.drawText(
            description_rect,
            Qt.AlignLeft | Qt.AlignTop | Qt.TextWordWrap,
            elided_description,
        )

        # end draw description
        painter.restore()


class CustomStepsListView(QListView):
    dropEventSignal = pyqtSignal(QModelIndex)

    def __init__(self, parent=None):
        super().__init__(parent)

    def dropEvent(self, e: QDropEvent):
        super().dropEvent(e)
        model_index = self.indexAt(e.pos())
        self.dropEventSignal.emit(model_index)
