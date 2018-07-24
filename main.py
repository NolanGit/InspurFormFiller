import re
import pyforms
import key_actions
from functools import reduce
from pyforms import BaseWidget
from pyforms.controls import ControlText
from pyforms.controls import ControlButton
from pyforms.controls import ControlCombo
from pypinyin import lazy_pinyin


class AutoFiller(BaseWidget):

    def __init__(self):
        super(AutoFiller, self).__init__('Auto Filler')
        self._project = ControlCombo('项目')
        self._project.add_item('后台')
        self._project.add_item('山东药监')
        self._project.add_item('沈阳药监')
        self._project.add_item('重庆药监')

        self._product = ControlCombo('产品')
        self._product.add_item('APP')
        self._product.add_item('行政执法')
        self._product.add_item('GIAP审批')
        self._product.add_item('食品日常检查')
        self._product.add_item('快速检验')
        self._product.add_item('药品日常检查')

        self._level = ControlCombo('严重程度')
        self._level.add_item('3-平均', 3)
        self._level.add_item('1-关键', 1)
        self._level.add_item('2-严重', 2)
        self._level.add_item('4-较轻', 4)

        self._type = ControlCombo('缺陷类型')
        self._type.add_item('1-功能性', 1)
        self._type.add_item('3-易用性', 3)

        self._person = ControlCombo('责任者')
        self._person.add_item('刘宝祥')
        self._person.add_item('厉见德')
        self._person.add_item('石志伟')

        self._button = ControlButton('确定')
        self._button.value = self.__buttonAction

        self.formset = [('_project', '_product'), ('_level', '_type'), ('_person', '_button')]

    def add_str(self, a, b):
        return a + b

    def project_action(self):
        length_of_letter = check(self._project.value)
        if length_of_letter == 0:
            pinyin_list = lazy_pinyin(self._project.value)
            pinyin = (reduce(self.add_str, pinyin_list))
            key_actions.string_to_key(pinyin)
            key_actions.space()
            key_actions.hold_time()
        else:
            letter_part = self._project.value[:length_of_letter]
            chinese_part = self._project.value[length_of_letter:]
            key_actions.caps()
            key_actions.string_to_key(letter_part)
            key_actions.caps()
            if len(chinese_part):
                pinyin_list = lazy_pinyin(chinese_part)
                pinyin = (reduce(self.add_str, pinyin_list))
                key_actions.string_to_key(pinyin)
                key_actions.space()
            key_actions.hold_time()

    def product_action(self):
        length_of_letter = check(self._product.value)
        if length_of_letter == 0:
            pinyin_list = lazy_pinyin(self._product.value)
            pinyin = (reduce(self.add_str, pinyin_list))
            key_actions.string_to_key(pinyin)
            key_actions.space()
            key_actions.hold_time()
        else:
            letter_part = self._product.value[:length_of_letter]
            chinese_part = self._product.value[length_of_letter:]
            key_actions.caps()
            key_actions.string_to_key(letter_part)
            key_actions.caps()
            if len(chinese_part):
                pinyin_list = lazy_pinyin(chinese_part)
                pinyin = (reduce(self.add_str, pinyin_list))
                key_actions.string_to_key(pinyin)
                key_actions.space()
            key_actions.hold_time()

    def level_action(self):
        if self._level.value == 1:
            key_actions.num_to_key(1)
            key_actions.minus()
            key_actions.string_to_key('guanjian')
        elif self._level.value == 2:
            key_actions.num_to_key(2)
            key_actions.minus()
            key_actions.string_to_key('yanzhong')
        elif self._level.value == 3:
            key_actions.num_to_key(3)
            key_actions.minus()
            key_actions.string_to_key('pingjun')
        elif self._level.value == 4:
            key_actions.num_to_key(4)
            key_actions.minus()
            key_actions.string_to_key('jiaoqing')
        key_actions.space()
        key_actions.hold_time()

    def type_action(self):
        if self._type.value == 1:
            key_actions.num_to_key(1)
            key_actions.minus()
            key_actions.string_to_key('gongnengxing')
        elif self._type.value == 3:
            key_actions.num_to_key(3)
            key_actions.minus()
            key_actions.string_to_key('yiyongxing')
        key_actions.space()
        key_actions.hold_time()

    def person_action(self):
        x = 0
        for x in range(5):
            key_actions.right()
            x += 1
        x = 0
        for x in range(5):
            key_actions.back()
            x += 1
        pinyin_list = lazy_pinyin(self._person.value)
        pinyin = (reduce(self.add_str, pinyin_list))
        key_actions.string_to_key(pinyin)
        key_actions.space()
        key_actions.hold_time()

    def __buttonAction(self):
        key_actions.alt_tab()
        self.project_action()
        key_actions.tab()
        key_actions.hold_time()
        self.product_action()
        key_actions.tab()
        key_actions.hold_time()
        self.level_action()
        key_actions.tab()
        key_actions.hold_time()
        self.type_action()
        key_actions.tab()
        key_actions.hold_time()
        key_actions.tab()
        key_actions.hold_time()
        self.person_action()


def check(str):
    my_re = re.compile(r'[A-Z]', re.S)
    res = re.findall(my_re, str)
    return len(res)

if __name__ == "__main__":
    pyforms.start_app(AutoFiller)
