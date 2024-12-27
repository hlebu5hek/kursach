from checkers.point import Point
from checkers.enums import CheckerType, SideType

# Сторона за которую играет игрок
PLAYER_SIDE = SideType.WHITE

AGAINST_BOT = True

# Размер поля
X_SIZE = Y_SIZE = 8
# Размер ячейки (в пикселях)
CELL_SIZE = 75

# Скорость анимации (больше = быстрее)
ANIMATION_SPEED = 6

# Количество ходов для предсказания
MAX_PREDICTION_DEPTH = 3

# Ширина рамки (Желательно должна быть чётной)
BORDER_WIDTH = 2 * 2

# Цвета игровой доски
FIELD_COLORS = ['#ffdfbf', '#040318']
# Цвет рамки при наведении на ячейку мышкой
HOVER_BORDER_COLOR = '#ad2340'
# Цвет рамки при выделении ячейки
SELECT_BORDER_COLOR = '#ad2340'
# Цвет кружков возможных ходов
POSIBLE_MOVE_CIRCLE_COLOR = '#ad2340'

# Возможные смещения ходов шашек
MOVE_OFFSETS = [
    Point(-1, -1),
    Point( 1, -1),
    Point(-1,  1),
    Point( 1,  1)
]

# Массивы типов белых и чёрных шашек [Обычная пешка, дамка]
WHITE_CHECKERS = [CheckerType.WHITE_REGULAR, CheckerType.WHITE_QUEEN]
BLACK_CHECKERS = [CheckerType.BLACK_REGULAR, CheckerType.BLACK_QUEEN]