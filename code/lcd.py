# Copyright (c) Quectel Wireless Solution, Co., Ltd.All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

LCD_INIT_DATA = bytes(
        (
            0, 0, 0x11,
            2, 0, 120,
            0, 1, 0x36,
            1, 1, 0x00,
            0, 1, 0x3A,
            1, 1, 0x05,
            0, 5, 0xB2,
            1, 1, 0x05,
            1, 1, 0x05,
            1, 1, 0x00,
            1, 1, 0x33,
            1, 1, 0x33,
            0, 1, 0xB7,
            1, 1, 0x75,
            0, 1, 0xBB,
            1, 1, 0x22,
            0, 1, 0xC0,
            1, 1, 0x2C,
            0, 1, 0xC2,
            1, 1, 0x01,
            0, 1, 0xC3,
            1, 1, 0x13,
            0, 1, 0xC4,
            1, 1, 0x20,
            0, 1, 0xC6,
            1, 1, 0x11,
            0, 2, 0xD0,
            1, 1, 0xA4,
            1, 1, 0xA1,
            0, 1, 0xD6,
            1, 1, 0xA1,
            0, 14, 0xE0,
            1, 1, 0xD0,
            1, 1, 0x05,
            1, 1, 0x0A,
            1, 1, 0x09,
            1, 1, 0x08,
            1, 1, 0x05,
            1, 1, 0x2E,
            1, 1, 0x44,
            1, 1, 0x45,
            1, 1, 0x0F,
            1, 1, 0x17,
            1, 1, 0x16,
            1, 1, 0x2B,
            1, 1, 0x33,
            0, 14, 0xE1,
            1, 1, 0xD0,
            1, 1, 0x05,
            1, 1, 0x0A,
            1, 1, 0x09,
            1, 1, 0x08,
            1, 1, 0x05,
            1, 1, 0x2E,
            1, 1, 0x43,
            1, 1, 0x45,
            1, 1, 0x0F,
            1, 1, 0x16,
            1, 1, 0x16,
            1, 1, 0x2B,
            1, 1, 0x33,
            0, 0, 0x29,
            0, 0, 0x21
        )
    )
LCD_INVALID = bytes(
        (
            0, 4, 0x2a,
            1, 1, 0xf0,
            1, 1, 0xf1,
            1, 1, 0xE0,
            1, 1, 0xE1,
            0, 4, 0x2b,
            1, 1, 0xf2,
            1, 1, 0xf3,
            1, 1, 0xE2,
            1, 1, 0xE3,
            0, 0, 0x2c,
        )
    )

LCD_DISPLAY_OFF = bytes(
        (
            0, 0, 0x11,
            2, 0, 20,
            0, 0, 0x29,
        )
    )

LCD_DISPLAY_ON = bytes(
        (
            0, 0, 0x28,
            2, 0, 120,
            0, 0, 0x10,
        )
    )

LCD_WIDTH = 240
# LCD_HEIGHT = 280
LCD_HEIGHT = 320
LCD_CLK = 26000
DATA_LINE = 1
LINE_NUM = 4
LCD_TYPE = 0
LCD_SET_BRIGHTNESS = None

CONTROL_PIN_NUMBER = 20
TE_PIN_NUMBER = 37


from machine import LCD
from machine import Pin
# from tp import gt9xx
import utime

gpio1 = Pin(Pin.GPIO27, Pin.OUT, Pin.PULL_PU, 1)
gpio2 = Pin(Pin.GPIO8, Pin.OUT, Pin.PULL_PU, 1)
gpio3 = Pin(Pin.GPIO11, Pin.OUT, Pin.PULL_PU, 1)
# en_pin = Pin(Pin.GPIO13, Pin.OUT, Pin.PULL_PU, 1)

mipilcd = LCD()

mipilcd.lcd_init(
            LCD_INIT_DATA,
            LCD_WIDTH,
            LCD_HEIGHT,
            LCD_CLK,
            DATA_LINE,
            LINE_NUM,
            LCD_TYPE,
            LCD_INVALID,
            LCD_DISPLAY_ON,
            LCD_DISPLAY_OFF,
            LCD_SET_BRIGHTNESS,
            )
mipilcd.lcd_clear(0x0000)

from tp import cst816 as Cst816
from machine import Pin,LCD 
import lvgl as lv

lv.init()
disp_buf1 = lv.disp_draw_buf_t()
buf1_1 = bytearray(LCD_WIDTH * LCD_HEIGHT * 2)
disp_buf1.init(buf1_1, None, len(buf1_1))
disp_drv = lv.disp_drv_t()
disp_drv.init()
disp_drv.draw_buf = disp_buf1
disp_drv.flush_cb =mipilcd.lcd_write
disp_drv.hor_res = LCD_WIDTH
disp_drv.ver_res = LCD_HEIGHT
# disp_drv.sw_rotate = 1
# disp_drv.rotated = lv.DISP_ROT._270  # 旋转角度
disp_drv.register()
# cst816初始化
Pin(31, Pin.OUT, Pin.PULL_DISABLE, 1)
tp_cst816 = Cst816(i2c_no=0, irq=44, reset=31, addr=0x15)
tp_cst816.init()
# self.tp_cst816.set_callback(self.ui_callback)
tp_cst816.activate()
print("cst816 init...")
# LVGL触摸注册
 # init input driver
indev_drv = lv.indev_drv_t()
indev_drv.init()
indev_drv.type = lv.INDEV_TYPE.POINTER
indev_drv.read_cb = tp_cst816.read
indev_drv.long_press_time = 400  # 400，表示长按的时间阈值，即按住一个点的时间超过该值时，触发长按事件。
indev_drv.scroll_limit = 10  # 10，表示在拖动对象之前，需要滑动的像素数。
indev_drv.scroll_throw = 10  # 10，表示滚动减速的百分比，值越大则减速越快。
indev_drv.gesture_limit = 10  # 50，表示手势滑动的阈值，即只有滑动偏移累计（绝对值）超过这个值才会触发手势动作。
indev_drv.gesture_min_velocity = 3  # 3，表示判断手势触发的最小差值。
indev_drv.register()
Pin(44, Pin.OUT, Pin.PULL_DISABLE, 0)

# image cache
lv.img.cache_invalidate_src(None)
lv.img.cache_set_size(50)

lv.tick_inc(5)
lv.task_handler()