import os
from pathlib import Path

from testing_adding_goods_to_cart import img as img_testing_adding_goods_to_cart
from testing_saucedemo_com import img as img_testing_saucedemo_com
from testing_demoqa_com import img as img_testing_demoqa_com

BASE_DIR = Path(__file__).parent
PATH_TO_ROOT = os.path.dirname(__file__)


PATH_TO_TESTING_ADDING_GOODS_TO_CART_IMG = os.path.join(Path(img_testing_adding_goods_to_cart.__file__).parent)
PATH_TO_TESTING_SAUCEDEMO_COM_IMG = os.path.join(Path(img_testing_saucedemo_com.__file__).parent)
PATH_TO_DEMOQA_COM_IMG = os.path.join(Path(img_testing_demoqa_com.__file__).parent)




