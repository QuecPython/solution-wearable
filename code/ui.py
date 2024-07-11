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

import lvgl as lv
import _thread
import utime
import osTimer



try:
    from css import *
    from common import Abstract
    from constant import WEEK_ALIA
    import EventMesh
except:
    from usr.css import *
    from usr.common import *
    from usr import EventMesh
    from usr.constant import WEEK_ALIA


def lv_obj(parent=None, pos=None, size=None, style=None, add_flag=None, clear_flag=None, flex_flow=None,
           flex_align=None, gap=None,
           style_bg_opa=None, style_border_width=None, style_border_color=None, align_to=None):
    _obj = lv.obj() if parent is None else lv.obj(parent)
    if flex_flow is not None:
        _obj.set_flex_flow(flex_flow)
    if flex_align is not None:
        _obj.set_flex_align(*flex_align)
    if pos is not None:
        _obj.set_pos(*pos)
    if size is not None:
        _obj.set_size(*size)
    if style is not None:
        for i in style:
            _obj.add_style(*i)
    if add_flag is not None:
        _obj.add_flag(add_flag)
    if clear_flag is not None:
        _obj.clear_flag(clear_flag)
    if style_bg_opa is not None:
        _obj.set_style_bg_opa(*style_bg_opa)
    if style_border_width is not None:
        _obj.set_style_border_width(*style_border_width)
    if style_border_color is not None:
        _obj.set_style_border_color(*style_border_color)
    if align_to is not None:
        _obj.align_to(*align_to)
    if gap is not None:
        _obj.set_style_pad_gap(*gap)
    return _obj


def lv_label(parent=None, pos=None, size=None, text=None, long_mode=None, style_text_align=None, style=None,
             align=None):
    _label = lv.label() if parent is None else lv.label(parent)
    if pos is not None:
        _label.set_pos(*pos)
    if size is not None:
        _label.set_size(*size)
    if text is not None:
        _label.set_text(text)
    if long_mode is not None:
        _label.set_long_mode(long_mode)
    if style_text_align is not None:
        _label.set_style_text_align(*style_text_align)
    if style is not None:
        for i in style:
            _label.add_style(*i)
    if align is not None:
        _label.align(*align)
    return _label


def lv_img(parent=None, pos=None, size=None, src=None, style=None, zoom=None, pivot=None, align=None, flag=None):
    _img = lv.img() if parent is None else lv.img(parent)
    if pos is not None:
        _img.set_pos(*pos)
    if size is not None:
        _img.set_size(*size)
    if src is not None:
        _img.set_src(src)
    if zoom is not None:
        _img.set_zoom(zoom)
    if style is not None:
        for i in style:
            _img.add_style(*i)
    if pivot is not None:
        _img.set_pivot(*pivot)
    if align is not None:
        _img.align(*align)
    if flag is not None:
        _img.add_flag(flag)
    return _img


def lv_list(parent=None, pos=None, size=None, style_pad_left=None, style_pad_top=None, style_pad_row=None, style=None):
    _list = lv.list() if parent is None else lv.list(parent)
    if pos is not None:
        _list.set_pos(*pos)
    if size is not None:
        _list.set_size(*size)
    if style_pad_left is not None:
        _list.set_style_pad_left(*style_pad_left)
    if style_pad_top is not None:
        _list.set_style_pad_top(*style_pad_top)
    if style_pad_row is not None:
        _list.set_style_pad_row(*style_pad_row)
    if style is not None:
        for i in style:
            _list.add_style(*i)
    return _list


def lv_btn(parent=None, pos=None, size=None, style=None, flex_flow=None,
           flex_align=None, gap=None):
    _btn = lv.btn() if parent is None else lv.btn(parent)
    if pos is not None:
        _btn.set_pos(*pos)
    if size is not None:
        _btn.set_size(*size)
    if style is not None:
        for i in style:
            _btn.add_style(*i)
    if flex_flow is not None:
        _btn.set_flex_flow(flex_flow)
    if flex_align is not None:
        _btn.set_flex_align(*flex_align)
    if gap is not None:
        _btn.set_style_pad_gap(*gap)
    return _btn


def lv_line(parent=None, pos=None, size=None, points=None, style=None):
    _line = lv.line() if parent is None else lv.line(parent)
    if pos is not None:
        _line.set_pos(*pos)
    if size is not None:
        _line.set_size(*size)
    if points is not None:
        _line.set_points(*points)
    if style is not None:
        for i in style:
            _line.add_style(*i)
    return _line


################################# tileview对象########################################
tileview_screen = lv.obj()
tileview = lv.tileview(tileview_screen)


# 事件处理函数
def event_handler(e):
    code = e.get_code()
    if code == lv.EVENT.VALUE_CHANGED:
        current_tile = e.get_target().get_tile_act()
        EventMesh.publish("load_tileview", (current_tile.get_x() / 240, current_tile.get_y() / 280))


# 为 tileview 添加事件处理
tileview.add_event_cb(event_handler, lv.EVENT.ALL, None)
# 注册事件回调
tileview.add_event_cb(event_handler, lv.EVENT.ALL, None)
# 设置 tileview 的有效滑动方向
tileview.set_scroll_dir(lv.DIR.HOR)
################################# main主页面 #########################################
tile1 = tileview.add_tile(1, 0, lv.DIR.RIGHT | lv.DIR.LEFT)
# tile1.set_user_data({"screen": "main_screen"})
main_screen = lv_obj(
    parent=tile1,
    size=(240, 280),
    style=[
        (style_main_screen, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.SCROLLED),
        (style_cont, lv.PART.MAIN | lv.STATE.DEFAULT),
    ],
)
main_top = lv_obj(
    parent=main_screen,
    size=(240, 34),
    style=[
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.SCROLLED),
        (style_header, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_gap_default, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_bar_top_main, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_flex_raw_between, lv.PART.MAIN | lv.STATE.DEFAULT),
    ]
)
main_top_cont_1 = lv_obj(
    parent=main_top,
    size=(88, 20),
    style=[
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.SCROLLED),
        (style_cont, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_gap_default, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_main_top_cont_1, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_flex_raw_between, lv.PART.MAIN | lv.STATE.DEFAULT),
    ]
)

main_top_cont_1_img_signal = lv_obj(
    parent=main_top_cont_1,
    size=(20, 20),
    style=[
        (style_img_signal, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_flex_raw, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_cont, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.SCROLLED),
        (style_pad_default, lv.PART.MAIN | lv.STATE.DEFAULT),
    ]
)
main_top_cont_1_label_operator = lv_label(
    parent=main_top_cont_1,
    size=(64, 19),
    text="中国移动",
    style=[
        (style_font_16, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_font_grey, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_flex_raw, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_cont, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.SCROLLED),
        (style_pad_default, lv.PART.MAIN | lv.STATE.DEFAULT),
    ]
)
main_top_cont_2 = lv_obj(
    parent=main_top,
    size=(48, 20),
    style=[
        (style_flex_raw_between, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_cont, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.SCROLLED),
        (style_gap_default, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_pad_default, lv.PART.MAIN | lv.STATE.DEFAULT),
    ]
)
main_top_cont_2_img_gps = lv_obj(
    parent=main_top_cont_2,
    size=(20, 20),
    style=[
        (style_img_gps, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_cont, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.SCROLLED),
        (style_gap_default, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_pad_default, lv.PART.MAIN | lv.STATE.DEFAULT),
    ]
)
main_top_cont_2_img_bat = lv_obj(
    parent=main_top_cont_2,
    size=(20, 20),
    style=[
        (style_img_bat, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_cont, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.SCROLLED),
        (style_gap_default, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_pad_default, lv.PART.MAIN | lv.STATE.DEFAULT),
    ]
)

main_content_cont_1 = lv_obj(
    parent=main_screen,
    size=(116, 200),
    pos=(19, 64),
    style=[
        (style_cont, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.SCROLLED),
        (style_gap_default, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_flex_column_between, lv.PART.MAIN | lv.STATE.DEFAULT)
    ]
)

main_content_cont_1_hour = lv_obj(
    parent=main_content_cont_1,
    size=(116, 100),
    style=[
        (style_cont, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.SCROLLED),
        (style_gap_default, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_pad_default, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_flex_raw_between, lv.PART.MAIN | lv.STATE.DEFAULT)
    ]
)

main_content_cont_1_hour_0 = lv_img(
    parent=main_content_cont_1_hour,
    size=(58, 100),
    src="U:/media/h0.png",
    style=[
        (style_cont, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.SCROLLED),
        (style_gap_default, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_pad_default, lv.PART.MAIN | lv.STATE.DEFAULT),
    ]
)
main_content_cont_1_hour_1 = lv_img(
    parent=main_content_cont_1_hour,
    size=(58, 100),
    src="U:/media/h8.png",
    style=[
        (style_cont, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.SCROLLED),
        (style_gap_default, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_pad_default, lv.PART.MAIN | lv.STATE.DEFAULT),
    ]
)

main_content_cont_1_m = lv_obj(
    parent=main_content_cont_1,
    size=(116, 100),
    style=[
        (style_cont, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.SCROLLED),
        (style_gap_default, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_pad_default, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_flex_raw_between, lv.PART.MAIN | lv.STATE.DEFAULT)
    ]
)

main_content_cont_1_m_0 = lv_img(
    parent=main_content_cont_1_m,
    size=(58, 100),
    src="U:/media/m0.png",
    style=[
        (style_cont, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.SCROLLED),
        (style_gap_default, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_pad_default, lv.PART.MAIN | lv.STATE.DEFAULT),
    ]
)
main_content_cont_1_m_1 = lv_img(
    parent=main_content_cont_1_m,
    size=(58, 100),
    src="U:/media/m8.png",
    style=[
        (style_cont, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.SCROLLED),
        (style_gap_default, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_pad_default, lv.PART.MAIN | lv.STATE.DEFAULT),
    ]
)
main_content_cont_2 = lv_obj(
    parent=main_screen,
    size=(41, 50),
    pos=(149, 76),
    style=[
        (style_cont, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.SCROLLED),
        (style_gap_default, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_flex_column_between, lv.PART.MAIN | lv.STATE.DEFAULT),
    ]
)
main_content_cont_2_label_date = lv_label(
    parent=main_content_cont_2,
    size=(41, 19),
    text="06.18",
    style=[
        (style_font_16, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_flex_raw, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_cont, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.SCROLLED),
        (style_pad_default, lv.PART.MAIN | lv.STATE.DEFAULT),
    ]
)
main_content_cont_2_label_week = lv_label(
    parent=main_content_cont_2,
    size=(41, 19),
    text="周五",
    style=[
        (style_font_16, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_flex_raw, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_cont, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.SCROLLED),
        (style_pad_default, lv.PART.MAIN | lv.STATE.DEFAULT),
    ]
)
# ################################# main主页面 #########################################
tile2 = tileview.add_tile(2, 0, lv.DIR.RIGHT | lv.DIR.LEFT)
# tile2.set_user_data({"screen": "watch_face_screen"})
watch_face_screen = lv_obj(
    parent=tile2,
    size=(240, 280),
    style=[
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.SCROLLED),
        (style_cont, lv.PART.MAIN | lv.STATE.DEFAULT),
        (screen_style, lv.PART.MAIN | lv.STATE.DEFAULT),
    ],
)
watch_face_content_cont_1 = lv_obj(
    parent=watch_face_screen,
    size=(230, 230),
    pos=(5, 39),
    style=[
        (style_cont, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_watch_face_bg, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.SCROLLED),
        (style_gap_default, lv.PART.MAIN | lv.STATE.DEFAULT)
    ]
)

watch_face_content_cont_1_hour = lv_obj(
    parent=watch_face_content_cont_1,
    size=(130, 100),
    pos=(49, 53),
    style=[
        (style_cont, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.SCROLLED),
        (style_gap_default, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_flex_raw_between, lv.PART.MAIN | lv.STATE.DEFAULT)
    ]
)

watch_face_content_cont_1_hour_0 = lv_img(
    parent=watch_face_content_cont_1_hour,
    size=(68, 100),
    src="U:/media/t0.png",
    style=[
        (style_cont, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.SCROLLED),
        (style_gap_default, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_pad_default, lv.PART.MAIN | lv.STATE.DEFAULT),
    ]
)
watch_face_content_cont_1_hour_1 = lv_img(
    parent=watch_face_content_cont_1_hour,
    size=(68, 100),
    src="U:/media/t1.png",
    style=[
        (style_cont, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.SCROLLED),
        (style_gap_default, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_pad_default, lv.PART.MAIN | lv.STATE.DEFAULT),
    ]
)

watch_face_cont_point_h = lv_img(
    parent=watch_face_content_cont_1,
    size=(12, 53),
    pivot=(5, 45),
    align=(lv.ALIGN.CENTER, 0, -23),
    src='U:/media/r-h.png',
    style=[
        (style_cont, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.SCROLLED),
        (style_gap_default, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_pad_default, lv.PART.MAIN | lv.STATE.DEFAULT),
    ]
)
watch_face_cont_point_m = lv_img(
    parent=watch_face_content_cont_1,
    size=(30, 115),
    pivot=(14, 108),
    align=(lv.ALIGN.CENTER, 0, -55),
    src='U:/media/r-m.png',
    style=[
        (style_cont, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.SCROLLED),
        (style_gap_default, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_pad_default, lv.PART.MAIN | lv.STATE.DEFAULT),
    ]
)
watch_face_cont_point_s = lv_img(
    parent=watch_face_content_cont_1,
    size=(14, 119),
    pivot=(6, 105),
    align=(lv.ALIGN.CENTER, 0, -50),
    src="U:/media/r-s.png",
    style=[
        (style_cont, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.SCROLLED),
        (style_gap_default, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_pad_default, lv.PART.MAIN | lv.STATE.DEFAULT),
    ]
)

watch_face_cont_2 = lv_obj(
    parent=watch_face_screen,
    size=(76, 16),
    pos=(82, 205),
    style=[
        (style_cont, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.SCROLLED),
        (style_gap_default, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_flex_raw_between, lv.PART.MAIN | lv.STATE.DEFAULT),
    ]
)
watch_face_cont_2_label_date = lv_label(
    parent=watch_face_cont_2,
    size=(lv.SIZE.CONTENT, 16),
    text="06.18",
    style=[
        (style_font_16, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_flex_raw, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_cont, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.SCROLLED),
        (style_pad_default, lv.PART.MAIN | lv.STATE.DEFAULT),
    ]
)
watch_face_cont_2_label_week = lv_label(
    parent=watch_face_cont_2,
    size=(lv.SIZE.CONTENT, 16),
    text="周五",
    style=[
        (style_font_16, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_flex_raw, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_cont, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.SCROLLED),
        (style_pad_default, lv.PART.MAIN | lv.STATE.DEFAULT),
    ]
)

# ################################# display_screen主页面 #########################################
tile0 = tileview.add_tile(0, 0, lv.DIR.RIGHT)
display_screen = lv_obj(
    parent=tile0,
    size=(240, 280),
    style=[
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.SCROLLED),
        (style_cont, lv.PART.MAIN | lv.STATE.DEFAULT),
        (screen_style, lv.PART.MAIN | lv.STATE.DEFAULT),
    ],
)

display_cont = lv_obj(
    parent=display_screen,
    size=(140, 156),
    pos=(50, 62),
    flex_flow=lv.FLEX_FLOW.COLUMN,
    flex_align=(lv.FLEX_ALIGN.SPACE_BETWEEN, lv.FLEX_ALIGN.CENTER, lv.FLEX_ALIGN.CENTER),
    style=[
        (style_cont, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.SCROLLED),
    ],
)
display_cont_1 = lv_obj(
    parent=display_cont,
    size=(140, 85),
    flex_flow=lv.FLEX_FLOW.COLUMN,
    flex_align=(lv.FLEX_ALIGN.SPACE_BETWEEN, lv.FLEX_ALIGN.CENTER, lv.FLEX_ALIGN.CENTER),
    style=[
        (style_cont, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.SCROLLED),
    ],
)
display_cont_1_time = lv_label(
    parent=display_cont_1,
    size=(140, 66),
    text="05:50",
    style=[
        (style_font_56, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_flex_raw, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_cont, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.SCROLLED),
        (style_pad_default, lv.PART.MAIN | lv.STATE.DEFAULT),
    ]
)

display_cont_1_cont_2 = lv_obj(
    parent=display_cont_1,
    size=(140, 19),
    flex_flow=lv.FLEX_FLOW.ROW,
    flex_align=(lv.FLEX_ALIGN.SPACE_BETWEEN, lv.FLEX_ALIGN.END, lv.FLEX_ALIGN.END),
    style=[
        (style_cont, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.SCROLLED),
        (style_gap_default, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_display_cont_1_cont_2, lv.PART.MAIN | lv.STATE.DEFAULT),
    ]
)
display_cont_1_cont_2_date = lv_label(
    parent=display_cont_1_cont_2,
    size=(lv.SIZE.CONTENT, 16),
    text="06.18",
    style=[
        (style_font_16, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_cont, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.SCROLLED),
        (style_pad_default, lv.PART.MAIN | lv.STATE.DEFAULT)
    ]
)
display_cont_1_cont_2_week = lv_label(
    parent=display_cont_1_cont_2,
    size=(lv.SIZE.CONTENT, 16),
    text="周五",
    style=[
        (style_font_16, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_flex_raw, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_cont, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.SCROLLED),
        (style_pad_default, lv.PART.MAIN | lv.STATE.DEFAULT),
    ]
)

display_cont_2 = lv_obj(
    parent=display_cont,
    size=(112, 35),
    flex_flow=lv.FLEX_FLOW.ROW,
    flex_align=(lv.FLEX_ALIGN.SPACE_BETWEEN, lv.FLEX_ALIGN.CENTER, lv.FLEX_ALIGN.CENTER),
    style=[
        (style_cont, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.SCROLLED),
        (style_gap_default, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_pad_default, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_display_cont_2, lv.PART.MAIN | lv.STATE.DEFAULT),
    ],
)

display_cont_2_img_notify = lv_img(
    parent=display_cont_2,
    size=(16, 16),
    align=(lv.ALIGN.CENTER, 0, 0),
    src="U:/media/bell-03.png",
    style=[
        (style_cont, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.SCROLLED),
        (style_gap_default, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_pad_default, lv.PART.MAIN | lv.STATE.DEFAULT),
    ]
)

display_cont_2_label_content = lv_label(
    parent=display_cont_2,
    size=(lv.SIZE.CONTENT, 16),
    text="暂无通知",
    style=[
        (style_font_16, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_cont, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.SCROLLED),
        (style_pad_default, lv.PART.MAIN | lv.STATE.DEFAULT),
    ]
)

# ################################# app_list_screen主页面 #########################################
tile3 = tileview.add_tile(3, 0, lv.DIR.RIGHT | lv.DIR.LEFT)
# tile3.set_user_data({"screen": "app_list_1_screen"})
app_list_screen = lv_obj(
    parent=tile3,
    size=(240, 280),
    style=[
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.SCROLLED),
        (style_cont, lv.PART.MAIN | lv.STATE.DEFAULT),
        (screen_style, lv.PART.MAIN | lv.STATE.DEFAULT),
    ],
)
app_list_cont = lv_obj(
    parent=app_list_screen,
    size=(240, 280),
    flex_flow=lv.FLEX_FLOW.ROW_WRAP,
    flex_align=(lv.FLEX_ALIGN.START, lv.FLEX_ALIGN.START, lv.FLEX_ALIGN.START),
    style=[
        (style_cont, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.SCROLLED),
        (style_app_list, lv.PART.MAIN | lv.STATE.DEFAULT),
    ],
)
# ################################# appl_list_2_screen主页面 #########################################
tile4 = tileview.add_tile(4, 0, lv.DIR.RIGHT | lv.DIR.LEFT)
# tile4.set_user_data({"screen": "app_list_2_screen"})
app_list2_screen = lv_obj(
    parent=tile4,
    size=(240, 280),
    style=[
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.SCROLLED),
        (style_cont, lv.PART.MAIN | lv.STATE.DEFAULT),
        (screen_style, lv.PART.MAIN | lv.STATE.DEFAULT),
    ],
)
app_list2_cont = lv_obj(
    parent=app_list2_screen,
    pos=(16, 16),
    size=(152, 272),
    gap=(16, 0),
    flex_flow=lv.FLEX_FLOW.COLUMN,
    flex_align=(lv.FLEX_ALIGN.START, lv.FLEX_ALIGN.START, lv.FLEX_ALIGN.START),
    style=[
        (style_cont, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.SCROLLED),
        (style_pad_default, lv.PART.SCROLLBAR | lv.STATE.SCROLLED),
    ],
)
# ################################# dail_screen主页面 #########################################
dail_screen = lv_obj(
    size=(240, 280),
    style=[
        (screen_style, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.SCROLLED),
    ],
)
dail_top = lv_obj(
    parent=dail_screen,
    size=(240, 34),
    flex_flow=lv.FLEX_FLOW.ROW,
    flex_align=(lv.FLEX_ALIGN.START, lv.FLEX_ALIGN.END, lv.FLEX_ALIGN.END),
    style=[
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.SCROLLED),
        (style_header, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_dail_top, lv.PART.MAIN | lv.STATE.DEFAULT),
    ]
)
dail_top_img_return = lv_img(
    parent=dail_top,
    size=(20, 20),
    flag=lv.obj.FLAG.CLICKABLE,
    src="U:/media/chevron-left.png"
)

dail_phone_label = lv_label(
    parent=dail_screen,
    pos=(0, 40),
    size=(240, 33),
    text="18175001940",
    long_mode=lv.label.LONG.WRAP,
    style_text_align=(lv.TEXT_ALIGN.CENTER, 0),
    style=[
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.SCROLLED),
        (style_font_28, lv.PART.MAIN | lv.STATE.DEFAULT),
    ]
)

dail_img_del = lv_img(
    parent=dail_screen,
    pos=(214, 47),
    size=(20, 20),
    flag=lv.obj.FLAG.CLICKABLE,
    src="U:/media/delete.png"
)
dail_content = lv_obj(
    parent=dail_screen,
    pos=(6, 80),
    size=(228, 194),
    gap=(6, 0),
    flex_flow=lv.FLEX_FLOW.ROW_WRAP,
    flex_align=(lv.FLEX_ALIGN.START, lv.FLEX_ALIGN.SPACE_BETWEEN, lv.FLEX_ALIGN.SPACE_BETWEEN),
    style=[
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.SCROLLED),
        (style_cont, lv.PART.MAIN | lv.STATE.DEFAULT),
    ]
)

# ################################# dail_screen主页面 #########################################
call_screen = lv_obj(
    size=(240, 280),
    style=[
        (screen_style, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.SCROLLED),
    ],
)
call_top = lv_obj(
    parent=call_screen,
    size=(240, 34),
    flex_flow=lv.FLEX_FLOW.ROW,
    flex_align=(lv.FLEX_ALIGN.SPACE_BETWEEN, lv.FLEX_ALIGN.END, lv.FLEX_ALIGN.END),
    style=[
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.SCROLLED),
        (style_header, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_dail_top, lv.PART.MAIN | lv.STATE.DEFAULT),
    ]
)
call_top_label_1 = lv_label(
    parent=call_top,
    size=(32, 19),
    text="电话",
    long_mode=lv.label.LONG.WRAP,
    style_text_align=(lv.TEXT_ALIGN.CENTER, 0),
    style=[
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.SCROLLED),
        (style_font_16, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_font_2094FA, lv.PART.MAIN | lv.STATE.DEFAULT),
    ]
)
call_top_label_2 = lv_label(
    parent=call_top,
    size=(42, 19),
    text="10:18",
    long_mode=lv.label.LONG.WRAP,
    style_text_align=(lv.TEXT_ALIGN.CENTER, 0),
    style=[
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.SCROLLED),
        (style_font_16, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_font_2094FA, lv.PART.MAIN | lv.STATE.DEFAULT),
    ]
)
call_content_label_1 = lv_label(
    parent=call_screen,
    pos=(0, 89),
    size=(240, 33),
    text="18175001940",
    long_mode=lv.label.LONG.WRAP,
    style_text_align=(lv.TEXT_ALIGN.CENTER, 0),
    style=[
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.SCROLLED),
        (style_font_28, lv.PART.MAIN | lv.STATE.DEFAULT)
    ]
)
call_content_label_2 = lv_label(
    parent=call_screen,
    size=(240, 18),
    pos=(0, 135),
    text="正在呼叫...",
    long_mode=lv.label.LONG.WRAP,
    style_text_align=(lv.TEXT_ALIGN.CENTER, 0),
    style=[
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.SCROLLED),
        (style_font_16, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_font_grey, lv.PART.MAIN | lv.STATE.DEFAULT)
    ]
)
call_content_img_cancel = lv_img(
    parent=call_screen,
    pos=(86, 192),
    size=(68, 68),
    flag=lv.obj.FLAG.CLICKABLE,
    src="U:/media/cancel.png"
)

call_content_img_receive = lv_img(
    parent=call_screen,
    pos=(152, 192),
    size=(68, 68),
    flag=lv.obj.FLAG.CLICKABLE,
    src="U:/media/receive.png"
)

# ################################# dail_screen主页面 #########################################
tile5 = tileview.add_tile(5, 0, lv.DIR.RIGHT | lv.DIR.LEFT)
measurement_heart_screen = lv_obj(
    parent=tile5,
    size=(240, 280),
    style=[
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.SCROLLED),
        (style_cont, lv.PART.MAIN | lv.STATE.DEFAULT),
        (screen_style, lv.PART.MAIN | lv.STATE.DEFAULT),
    ],
)
tile6 = tileview.add_tile(6, 0, lv.DIR.RIGHT | lv.DIR.LEFT)
measurement_blood_screen = lv_obj(
    parent=tile6,
    size=(240, 280),
    style=[
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.SCROLLED),
        (style_cont, lv.PART.MAIN | lv.STATE.DEFAULT),
        (screen_style, lv.PART.MAIN | lv.STATE.DEFAULT),
    ],
)
tile7 = tileview.add_tile(7, 0, lv.DIR.LEFT)
measurement_temp_screen = lv_obj(
    parent=tile7,
    size=(240, 280),
    style=[
        (screen_style, lv.PART.MAIN | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT),
        (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.SCROLLED),
        (style_cont, lv.PART.MAIN | lv.STATE.DEFAULT),
        (screen_style, lv.PART.MAIN | lv.STATE.DEFAULT),
    ],
)


class Screen(Abstract):
    def __init__(self):
        self.meta = None
        self.prop = None
        self.last_screen_info = None

    def move_up(self):
        pass

    def move_left(self):
        pass

    def move_right(self):
        pass

    def move_down(self):
        pass

    def set_prop(self, prop):
        self.prop = prop


class MainScreen(Screen):
    NAME = "main_screen"

    def __init__(self):
        super().__init__()
        self.meta = main_screen
        self.ele_hour_0 = main_content_cont_1_hour_0
        self.ele_hour_1 = main_content_cont_1_hour_1
        self.ele_min_0 = main_content_cont_1_m_0
        self.ele_min_1 = main_content_cont_1_m_1
        self.ele_date = main_content_cont_2_label_date
        self.ele_week = main_content_cont_2_label_week

    def post_processor_before_initialization(self, *args, **kwargs):
        main_top.set_parent(self.meta)
        EventMesh.subscribe("topic_time", self.do_update_time)

    def do_update_time(self, event=None, msg=None):
        current_time = utime.localtime()
        hour, minute = current_time[3], current_time[4]
        date = "{:02d}".format(current_time[1]) + "." + "{:02d}".format(current_time[2])
        h1 = hour // 10
        h2 = hour % 10
        m1 = minute // 10
        m2 = minute % 10
        self.ele_hour_0.set_src("U:/media/h{}.png".format(h1))
        self.ele_hour_1.set_src("U:/media/h{}.png".format(h2))
        self.ele_min_0.set_src("U:/media/m{}.png".format(m1))
        self.ele_min_1.set_src("U:/media/m{}.png".format(m2))
        self.ele_date.set_text(date)
        self.ele_week.set_text(WEEK_ALIA[current_time[-2]])

    def initialization(self, *args, **kwargs):
        self.do_update_time()


class DisplayScreen(Screen):
    NAME = "display_screen"

    def __init__(self):
        super().__init__()
        self.meta = display_screen
        self.ele_time = display_cont_1_time
        self.ele_date = display_cont_1_cont_2_date
        self.ele_week = display_cont_1_cont_2_week

    def post_processor_before_initialization(self, *args, **kwargs):
        EventMesh.subscribe("topic_time", self.do_update_time)

    def do_update_time(self, event=None, msg=None):
        current_time = utime.localtime()
        hour, minute = current_time[3], current_time[4]
        date = "{:02d}".format(current_time[1]) + "." + "{:02d}".format(current_time[2])
        _time = "{:02d}".format(hour) + ":" + "{:02d}".format(minute)
        self.ele_time.set_text(_time)
        self.ele_date.set_text(date)
        self.ele_week.set_text(WEEK_ALIA[current_time[-2]])

    def initialization(self, *args, **kwargs):
        self.do_update_time()


class WatchFaceScreen(Screen):
    NAME = "watch_face_screen"

    def __init__(self):
        super().__init__()
        self.meta = watch_face_screen
        self.ele_hour = watch_face_cont_point_h
        self.ele_min = watch_face_cont_point_m
        self.ele_sec = watch_face_cont_point_s
        self.ele_hour_cont_1 = watch_face_content_cont_1_hour_0
        self.ele_hour_cont_2 = watch_face_content_cont_1_hour_1
        self.ele_date = watch_face_cont_2_label_date
        self.ele_week = watch_face_cont_2_label_week
        self.ele_hour_cont_1_num = 0
        self.ele_hour_cont_2_num = 0
        self.second = 0
        self.minute = 0
        self.hour = 0
        self.date = "00.00"
        self.week = 0
        self.flag = False
        self.run_flag = False

    def post_processor_before_initialization(self, *args, **kwargs):
        main_top.set_parent(self.meta)

    def initialization(self):
        self.ele_hour_cont_1_num = 0
        self.ele_hour_cont_2_num = 0
        self.date = "00.00"
        self.week = 0
        current_time = utime.localtime()
        self.hour, self.minute, self.second = current_time[3], current_time[4], current_time[5]
        self.date = "{:02d}".format(current_time[1]) + "." + "{:02d}".format(current_time[2])
        self.week = current_time[-2]
        self.flag = True
        self.do_update_time()
        self.do_update_hour_cont()
        self.do_update_date()
        self.do_update_week()
        if self.flag and not self.run_flag:
            _thread.start_new_thread(self.do_strategy_update_time, ())

    def deactivate(self):
        self.flag = False

    def do_update_date(self, *args):
        self.ele_date.set_text(self.date)

    def do_update_week(self, *args):
        self.ele_week.set_text(WEEK_ALIA[self.week])

    def do_strategy_update_time(self, *args):
        while True:
            if not self.flag:
                self.run_flag = False
                break
            else:
                utime.sleep(1)
                self.do_strategy_calc_time()
                self.do_update_hour_cont()
                self.do_update_time()

    def do_update_hour_cont(self):
        h1 = self.hour // 10
        h2 = self.hour % 10
        if h1 != self.ele_hour_cont_1_num:
            self.ele_hour_cont_1_num = h1
            self.ele_hour_cont_1.set_src("U:/media/t{}.png".format(self.ele_hour_cont_1_num))
        if h2 != self.ele_hour_cont_2_num:
            self.ele_hour_cont_2_num = h2
            self.ele_hour_cont_2.set_src("U:/media/t{}.png".format(self.ele_hour_cont_2_num))

    def do_update_time(self):
        hour, minute, second = self.update_clock_angles(self.hour, self.minute, self.second)
        # print(hour, minute, second)
        self.ele_hour.set_angle(int(hour * 10))
        self.ele_min.set_angle(int(minute * 10))
        self.ele_sec.set_angle(int(second * 10))

    def do_strategy_calc_time(self):
        self.second += 1
        if self.second >= 60:
            self.second = 0
            self.minute += 1
        if self.minute >= 60:
            self.minute = 0
            self.hour = (self.hour + 1) % 24

    def update_clock_angles(self, hours, minutes, seconds):
        second_angle = (seconds * 6) % 360
        minute_angle = (minutes * 6 + seconds * 0.1) % 360
        hour_angle = ((hours % 12) * 30 + minutes * 0.5 + seconds * (0.5 / 60)) % 360
        return hour_angle, minute_angle, second_angle


class AppList1Screen(Screen):
    NAME = "app_list_1_screen"

    def __init__(self):
        super().__init__()
        self.meta = app_list_screen
        self.container = app_list_cont
        self.profile = [
            ["U:/media/app_heart.png", {"screen": "blood_screen"}],
            ["U:/media/app_phone.png", {"screen": "dail_screen"}],
            ["U:/media/app_chat.png", None],
            ["U:/media/app_time.png", None]
        ]
        self.btn_list = []
        self.bottom = None
        self.bottom_profile = [
            ["U:/media/wpoint.png"],
            ["U:/media/bpoint.png"],
            ["U:/media/bpoint.png"],
            ["U:/media/bpoint.png"]
        ]
        self.bottom_btn_list = []

    def btn_click(self, event, i):
        screen_info = self.profile[i][1]
        if screen_info:
            EventMesh.publish("load_screen", screen_info)

    def post_processor_after_instantiation(self):
        for i, btn_profile in enumerate(self.profile):
            btn = lv_img(
                parent=self.container,
                size=(110, 110),
                src=btn_profile[0],
                flag=lv.obj.FLAG.CLICKABLE,
                style=[
                    (style_cont, lv.PART.MAIN | lv.STATE.DEFAULT),
                    (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT),
                    (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.SCROLLED),
                    (style_gap_default, lv.PART.MAIN | lv.STATE.DEFAULT),
                    (style_pad_default, lv.PART.MAIN | lv.STATE.DEFAULT),
                ]
            )
            btn.add_event_cb(lambda event, cur=i: self.btn_click(event, cur), lv.EVENT.CLICKED, None)
            self.btn_list.append(btn)
        self.bottom = lv_obj(
            parent=app_list_screen,
            pos=(88, 254),
            size=(56, 8),
            flex_flow=lv.FLEX_FLOW.ROW,
            flex_align=(lv.FLEX_ALIGN.SPACE_AROUND, lv.FLEX_ALIGN.START, lv.FLEX_ALIGN.START),
            style=[
                (style_cont, lv.PART.MAIN | lv.STATE.DEFAULT),
                (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT),
                (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.SCROLLED),
                (style_pad_default, lv.PART.SCROLLBAR | lv.STATE.SCROLLED),
                (style_app_list, lv.PART.MAIN | lv.STATE.DEFAULT),
            ],
        )
        for btn_profile in self.bottom_profile:
            btn = lv_img(
                parent=self.bottom,
                size=(8, 8),
                src=btn_profile[0],
                style=[
                    (style_cont, lv.PART.MAIN | lv.STATE.DEFAULT),
                    (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT),
                    (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.SCROLLED),
                    (style_gap_default, lv.PART.MAIN | lv.STATE.DEFAULT),
                    (style_pad_default, lv.PART.MAIN | lv.STATE.DEFAULT),
                ]
            )
            self.bottom_btn_list.append(btn)


class AppList2Screen(Screen):
    NAME = "app_list_2_screen"

    def __init__(self):
        super().__init__()
        self.meta = app_list2_screen
        self.container = app_list2_cont
        self.profile = [
            ["U:/media/heart2.png", (style_bg_color_ff5035, lv.PART.MAIN | lv.STATE.DEFAULT), "心率",
             {"screen": "blood_screen"}],
            ["U:/media/phone2.png", (style_bg_color_2094FA, lv.PART.MAIN | lv.STATE.DEFAULT), "电话",
             {"screen": "dail_screen"}],
            ["U:/media/chat2.png", (style_bg_color_42BF4B, lv.PART.MAIN | lv.STATE.DEFAULT), "微聊", None],
            ["U:/media/calc_time2.png", (style_bg_color_FFB342, lv.PART.MAIN | lv.STATE.DEFAULT), "倒计时", None]
        ]
        self.btn_list = []

    def btn_click(self, event, i):
        screen_info = self.profile[i][-1]
        if screen_info:
            EventMesh.publish("load_screen", screen_info)

    def post_processor_after_instantiation(self):
        for i, btn_profile in enumerate(self.profile):
            btn = lv_btn(
                parent=self.container,
                size=(152, 56),
                flex_flow=lv.FLEX_FLOW.ROW_WRAP,
                flex_align=(lv.FLEX_ALIGN.START, lv.FLEX_ALIGN.CENTER, lv.FLEX_ALIGN.CENTER),
                gap=(24, 0),
                style=[
                    (style_btn, lv.PART.MAIN | lv.STATE.DEFAULT),
                    (style_cont, lv.PART.MAIN | lv.STATE.DEFAULT),
                    (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT),
                    (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.SCROLLED),
                ],
            )
            btn.add_event_cb(lambda event, cur=i: self.btn_click(event, cur), lv.EVENT.CLICKED, None)
            btn_circle = lv_obj(
                parent=btn,
                size=(56, 56),
                style=[
                    # (style_cont, lv.PART.MAIN | lv.STATE.DEFAULT),
                    (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT),
                    (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.SCROLLED),
                    (style_gap_default, lv.PART.MAIN | lv.STATE.DEFAULT),
                    (style_circle_max, lv.PART.MAIN | lv.STATE.DEFAULT),
                    btn_profile[1]
                ],
            )
            btn_circle_img = lv_img(
                parent=btn_circle,
                size=(56, 56),
                src=btn_profile[0]
            )
            btn_label = lv_label(
                parent=btn,
                text=btn_profile[2],
                size=(lv.SIZE.CONTENT, 28),
                long_mode=lv.label.LONG.WRAP,
                style=[
                    (style_font_16, lv.PART.MAIN | lv.STATE.DEFAULT),
                ]
            )
            self.btn_list.append((btn, btn_circle, btn_circle_img, btn_label))


class DailScreen(Screen):
    NAME = "dail_screen"

    def __init__(self):
        super().__init__()
        self.meta = dail_screen
        self.container = dail_content
        self.ele_r = dail_top_img_return
        self.ele_phone = dail_phone_label
        self.ele_del = dail_img_del
        self.profile = [
            (1, "U:/media/b1.png"),
            (2, "U:/media/b2.png"),
            (3, "U:/media/b3.png"),
            (4, "U:/media/b4.png"),
            (5, "U:/media/b5.png"),
            (6, "U:/media/b6.png"),
            (7, "U:/media/b7.png"),
            (8, "U:/media/b8.png"),
            (9, "U:/media/b9.png"),
            (-1, "U:/media/None.png"),
            (0, "U:/media/b0.png"),
            (10, "U:/media/b10.png"),
        ]
        self.btn_list = []
        self.phone_number = ""
        self.ele_del.add_event_cb(lambda event: self.reduce_phone_number(event), lv.EVENT.CLICKED, None)
        self.ele_r.add_event_cb(lambda event: self.do_return(event), lv.EVENT.CLICKED, None)

    def do_return(self, *args):
        EventMesh.publish("load_screen", self.last_screen_info)

    def add_phone_number(self, number):
        if len(self.phone_number) < 11:
            self.phone_number += str(number)
            self.ele_phone.set_text(self.phone_number)

    def reduce_phone_number(self, *args):
        if self.phone_number:
            self.phone_number = self.phone_number[:len(self.phone_number) - 1]
        else:
            self.phone_number = ""
        self.ele_phone.set_text(self.phone_number)

    def post_processor_after_instantiation(self):
        for btn_profile in self.profile:
            btn = lv_img(
                parent=self.container,
                size=(72, 44),
                src=btn_profile[1],
                flag=lv.obj.FLAG.CLICKABLE
            )
            btn.add_event_cb(lambda event, cur=btn_profile[0]: self.btn_click(event, cur), lv.EVENT.CLICKED, None)
            self.btn_list.append(btn)

    def initialization(self, *args, **kwargs):
        if self.prop.get("init", True):
            self.phone_number = ""
            self.ele_phone.set_text(self.phone_number)

    def btn_click(self, event, cur):
        if cur == -1:
            return
        if cur == 10:
            if self.phone_number:
                EventMesh.publish("load_screen", {"screen": "call_screen", "mode": 0, "phone": self.phone_number})
                return
        else:
            self.add_phone_number(cur)


class CallScreen(Screen):
    NAME = "call_screen"

    class Mode:
        CALL = 0
        INCOMING = 1
        ANSWER = 2

    def __init__(self):
        super().__init__()
        self.meta = call_screen
        self.ele_cont_label_1 = call_content_label_1
        self.ele_cont_label_2 = call_content_label_2
        self.ele_img_cancel = call_content_img_cancel
        self.ele_img_receive = call_content_img_receive
        self.m = 0
        self.s = 0
        self.phone = ""
        self.timer = osTimer()
        self.ele_img_cancel.add_event_cb(self.do_cancel, lv.EVENT.CLICKED, None)
        self.ele_img_receive.add_event_cb(self.do_incomming_answer, lv.EVENT.CLICKED, None)

    def do_incomming_answer(self, *args):
        self.do_answer()

    def do_cancel(self, *args):
        self.last_screen_info.update({"init": False})
        EventMesh.publish("load_screen", {"screen":"app_list_2_screen"})

    def do_call(self, des=None):
        self.ele_cont_label_1.set_pos(0, 89)
        self.ele_cont_label_2.set_pos(0, 135)
        if des is None:
            self.ele_cont_label_2.set_text("正在呼叫...")
        self.ele_cont_label_1.set_text(self.phone)
        self.ele_img_cancel.set_pos(86, 192)
        self.ele_img_receive.add_flag(lv.obj.FLAG.HIDDEN)

    def do_incoming(self, des=None):
        self.ele_cont_label_1.set_pos(0, 89)
        self.ele_cont_label_2.set_pos(0, 135)
        if des is None:
            self.ele_cont_label_2.set_text("来电")
        self.ele_cont_label_1.set_text(self.phone)
        self.ele_img_cancel.set_pos(20, 192)
        self.ele_img_receive.clear_flag(lv.obj.FLAG.HIDDEN)

    def do_answer(self, des=None):
        self.ele_cont_label_1.set_pos(0, 115)
        self.ele_cont_label_2.set_pos(0, 84)
        self.ele_cont_label_2.set_text(self.phone)
        self.ele_img_cancel.set_pos(86, 192)
        self.ele_cont_label_1.set_text("{:02d}:{:02d}".format(self.m, self.s))
        self.ele_img_receive.add_flag(lv.obj.FLAG.HIDDEN)
        self.timer.start(1000, 1, self.do_increase_time)

    def do_increase_time(self, *args):
        self.s += 1
        if self.s >= 60:
            self.s = 0
            self.m += 1
        self.ele_cont_label_1.set_text("{:02d}:{:02d}".format(self.m, self.s))

    def deactivate(self):
        self.timer.stop()

    def initialization(self):
        if self.prop["mode"] == self.Mode.CALL:
            self.phone = self.prop["phone"]
            self.do_call()


class MeasurementScreen(Screen):
    def __init__(self):
        super().__init__()
        self.meta = None
        self.ele_top = None
        self.ele_top_cont = None
        self.ele_top_img_return = None
        self.ele_top_title = None
        self.ele_top_time = None
        self.ele_content_img = None
        self.ele_content_label = None
        self.ele_content_start_label = None
        self.ele_content_btn = None
        self.ele_content_btn_label = None
        self.profile = {
            "top": [
                ("U:/media/chevron-left-r.png",),
                ("血氧", lv.color_hex(0xFFB342))
            ],
            "content": [
                ("U:/media/blood-rounded.png",)
            ],
            "btn": [
                ("正在测量", lv.color_hex(0xFFB342))
            ]
        }
        self.count = 1
        self.timer = osTimer()

    def post_processor_after_instantiation(self, *args, **kwargs):
        self.ele_top = lv_obj(
            parent=self.meta,
            size=(240, 34),
            flex_flow=lv.FLEX_FLOW.ROW,
            flex_align=(lv.FLEX_ALIGN.SPACE_BETWEEN, lv.FLEX_ALIGN.END, lv.FLEX_ALIGN.END),
            style=[
                (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT),
                (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.SCROLLED),
                (style_header, lv.PART.MAIN | lv.STATE.DEFAULT),
                (style_dail_top, lv.PART.MAIN | lv.STATE.DEFAULT),
            ]
        )

        self.ele_top_cont = lv_obj(
            parent=self.ele_top,
            size=(52, 20),
            flex_flow=lv.FLEX_FLOW.ROW,
            flex_align=(lv.FLEX_ALIGN.SPACE_BETWEEN, lv.FLEX_ALIGN.END, lv.FLEX_ALIGN.END),
            style=[
                (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT),
                (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.SCROLLED),
                (style_cont, lv.PART.MAIN | lv.STATE.DEFAULT),
            ]
        )

        self.ele_top_img_return = lv_img(
            parent=self.ele_top_cont,
            size=(20, 20),
            src="U:/media/chevron-left-r.png"
        )
        self.ele_top_title = lv_label(
            parent=self.ele_top_cont,
            size=(32, 19),
            text="心率",
            long_mode=lv.label.LONG.WRAP,
            style_text_align=(lv.TEXT_ALIGN.CENTER, 0),
            style=[
                (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT),
                (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.SCROLLED),
                (style_font_16, lv.PART.MAIN | lv.STATE.DEFAULT),
                (style_font_ff5035, lv.PART.MAIN | lv.STATE.DEFAULT),
            ]
        )

        self.ele_top_time = lv_label(
            parent=self.ele_top,
            size=(42, 19),
            text="10:18",
            long_mode=lv.label.LONG.WRAP,
            style=[
                (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT),
                (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.SCROLLED),
                (style_font_16, lv.PART.MAIN | lv.STATE.DEFAULT),
            ]
        )

        self.ele_content_img = lv_img(
            parent=self.meta,
            size=(100, 100),
            pos=(70, 70),
            src="U:/media/blood-rounded.png"
        )

        self.ele_content_label = lv_label(
            parent=self.meta,
            size=(240, 19),
            pos=(0, 200),
            text="64次/分 (10分钟前)",
            long_mode=lv.label.LONG.WRAP,
            style_text_align=(lv.TEXT_ALIGN.CENTER, 0),
            style=[
                (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT),
                (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.SCROLLED),
                (style_font_16, lv.PART.MAIN | lv.STATE.DEFAULT),
            ]
        )
        self.ele_content_start_label = lv_label(
            parent=self.meta,
            size=(240, 23),
            pos=(0, 200),
            text="正在测量...",
            long_mode=lv.label.LONG.WRAP,
            style_text_align=(lv.TEXT_ALIGN.CENTER, 0),
            style=[
                (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT),
                (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.SCROLLED),
                (style_font_16, lv.PART.MAIN | lv.STATE.DEFAULT),
            ]
        )

        self.ele_content_btn = lv_obj(
            parent=self.meta,
            pos=(6, 230),
            size=(224, 44),
            style=[
                # (style_cont, lv.PART.MAIN | lv.STATE.DEFAULT),
                (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT),
                (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.SCROLLED),
                (style_gap_default, lv.PART.MAIN | lv.STATE.DEFAULT),
                (style_circle_22, lv.PART.MAIN | lv.STATE.DEFAULT),
                (style_bg_color_262626, lv.PART.MAIN | lv.STATE.DEFAULT)
            ],
        )
        self.ele_content_btn.add_event_cb(self.btn_click, lv.EVENT.CLICKED, None)
        self.ele_top_cont.add_event_cb(self.do_return, lv.EVENT.CLICKED, None)
        self.ele_content_btn_label = lv_label(
            parent=self.ele_content_btn,
            size=(64, 19),
            text="开始测量",
            long_mode=lv.label.LONG.WRAP,
            align=(lv.ALIGN.CENTER, 0, 0),
            style=[
                (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.DEFAULT),
                (style_list_scrollbar, lv.PART.SCROLLBAR | lv.STATE.SCROLLED),
                (style_font_16, lv.PART.MAIN | lv.STATE.DEFAULT),
            ]
        )

    def do_return(self, *args):
        EventMesh.publish("load_screen", {"screen":"app_list_2_screen"})

    def btn_click(self, *args):
        self.do_start()

    def init_header(self):
        self.ele_content_btn.clear_flag(lv.obj.FLAG.HIDDEN)
        self.ele_content_label.clear_flag(lv.obj.FLAG.HIDDEN)
        self.ele_content_start_label.add_flag(lv.obj.FLAG.HIDDEN)
        # 设置返回的标识
        self.ele_top_img_return.set_src(self.profile["top"][0][0])
        # 设置标题字体和颜色
        self.ele_top_title.set_text(self.profile["top"][1][0])
        self.ele_top_title.set_style_text_color(self.profile["top"][1][1], lv.PART.MAIN | lv.STATE.DEFAULT)
        # 设置内容图片
        self.ele_content_img.set_src(self.profile["content"][0][0])
        # 设置btn的字体颜色
        self.ele_content_btn_label.set_text(self.profile["btn"][0][0])
        self.ele_content_btn_label.set_style_text_color(self.profile["btn"][0][1], lv.PART.MAIN | lv.STATE.DEFAULT)

    def do_start(self):
        self.ele_content_label.add_flag(lv.obj.FLAG.HIDDEN)
        self.ele_content_btn.add_flag(lv.obj.FLAG.HIDDEN)
        self.ele_content_start_label.clear_flag(lv.obj.FLAG.HIDDEN)
        self.ele_content_start_label.set_text("正在测量" + "." * self.count)
        self.timer.start(1000, 1, self.do_start_label_update)

    def set_content(self, content):
        self.ele_content_label.set_text(content)

    def do_start_label_update(self, *args):
        self.count += 1
        if self.count >= 4:
            self.count = 1
        self.ele_content_start_label.set_text("正在测量" + "." * self.count)

    def deactivate(self):
        self.timer.stop()


class BloodScreen(MeasurementScreen):
    NAME = "blood_screen"

    def __init__(self):
        super().__init__()
        self.meta = measurement_blood_screen
        self.profile = {
            "top": [
                ("U:/media/chevron-left-r.png",),
                ("血氧", lv.color_hex(0xFF352B))
            ],
            "content": [
                ("U:/media/blood-rounded.png",)
            ],
            "btn": [
                ("正在测量", lv.color_hex(0xFF352B))
            ]
        }

    def initialization(self):
        self.init_header()
        self.set_content("98% (10分钟前)")


class TempScreen(MeasurementScreen):
    NAME = "temp_screen"

    def __init__(self):
        super().__init__()
        self.meta = measurement_temp_screen
        self.profile = {
            "top": [
                ("U:/media/chevron-left-y.png",),
                ("体温", lv.color_hex(0xFFB342))
            ],
            "content": [
                ("U:/media/temp-rounded.png",)
            ],
            "btn": [
                ("正在测量", lv.color_hex(0xFFB342))
            ]
        }

    def initialization(self):
        self.init_header()
        self.set_content("36.5℃ (10分钟前)")


class HeartScreen(MeasurementScreen):
    NAME = "heart_screen"

    def __init__(self):
        super().__init__()
        self.meta = measurement_heart_screen
        self.profile = {
            "top": [
                ("U:/media/chevron-left-r-1.png",),
                ("心率", lv.color_hex(0xFF5035))
            ],
            "content": [
                ("U:/media/heart-rounded.png",)
            ],
            "btn": [
                ("正在测量", lv.color_hex(0xFF5035))
            ]
        }

    def initialization(self):
        self.init_header()
        self.set_content("64次/分 (10分钟前)")


normal_style = lv.style_t()
normal_style.set_border_width(0)
normal_style.set_pad_all(0)
normal_style.set_outline_width(0)
normal_style.set_text_color(lv.color_white())
normal_style.set_radius(0)
normal_style.set_bg_color(lv.color_black())


class CountDownSettingScreen(Screen):
    NAME = 'countdown_screen'

    def __init__(self):
        super().__init__()

        self.meta = lv.obj()
        self.meta.add_style(normal_style, 0)

        self.rt_img = lv.img(self.meta, src='E:/media/chevron-left-y.png')
        self.rt_img.set_align(lv.ALIGN.TOP_LEFT)
        self.rt_label = lv.label(self.meta)
        self.rt_label.set_text('设置')
        self.rt_label.set_style_text_color(lv.palette_main(lv.PALETTE.YELLOW), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.rt_label.align_to(self.rt_img, lv.ALIGN.OUT_RIGHT_MID, 5, 0)
        self.time = lv.label(self.meta)
        self.time.set_text('09:00')
        self.time.set_align(lv.ALIGN.TOP_RIGHT)

        self.layout = lv.obj(self.meta)
        self.layout.set_size(240, 250)
        self.layout.set_y(30)
        self.layout.set_layout(lv.LAYOUT_FLEX.value)
        self.layout.set_style_flex_flow(lv.FLEX_FLOW.ROW_WRAP, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.layout.set_style_flex_main_place(lv.FLEX_ALIGN.SPACE_EVENLY, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.layout.set_style_flex_cross_place(lv.FLEX_ALIGN.CENTER, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.layout.set_style_flex_track_place(lv.FLEX_ALIGN.SPACE_EVENLY, lv.PART.MAIN | lv.STATE.DEFAULT)

        self.layout.add_style(normal_style, lv.PART.MAIN | lv.STATE.DEFAULT)

        self.hours_label = lv.label(self.layout)
        self.hours_label.set_text('小时')
        self.hours_label.set_style_text_color(lv.palette_main(lv.PALETTE.YELLOW), lv.PART.MAIN | lv.STATE.DEFAULT)

        self.minutes_label = lv.label(self.layout)
        self.minutes_label.set_text('分钟')
        self.minutes_label.set_style_text_color(lv.palette_main(lv.PALETTE.YELLOW), lv.PART.MAIN | lv.STATE.DEFAULT)

        self.seconds_label = lv.label(self.layout)
        self.seconds_label.set_text('秒')
        self.seconds_label.set_style_text_color(lv.palette_main(lv.PALETTE.YELLOW), lv.PART.MAIN | lv.STATE.DEFAULT)

        self.roller_hours = lv.roller(self.layout)
        self.roller_hours.set_options("\n".join(['{:02d}'.format(hour) for hour in range(24)]), lv.roller.MODE.NORMAL)
        self.roller_hours.set_visible_row_count(3)
        self.roller_hours.set_style_border_width(0, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.roller_hours.set_style_text_color(lv.color_white(), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.roller_hours.set_style_bg_color(lv.color_black(), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.roller_hours.set_style_bg_opa(lv.OPA.TRANSP, lv.PART.SELECTED | lv.STATE.DEFAULT)
        self.roller_hours.set_style_pad_all(0, lv.PART.MAIN | lv.STATE.DEFAULT)

        self.roller_hours.add_flag(lv.OBJ_FLAG_FLEX_IN_NEW.TRACK)
        self.roller_hours.set_style_text_opa(lv.OPA.COVER, lv.PART.SELECTED | lv.STATE.DEFAULT)
        self.roller_hours.set_style_text_opa(lv.OPA._80, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.roller_hours.add_event_cb(
            lambda event: print('roller_hours VALUE_CHANGED'),
            lv.EVENT.VALUE_CHANGED,
            None
        )
        self.sep1 = lv.label(self.layout)
        self.sep1.set_text(':')

        self.roller_minutes = lv.roller(self.layout)
        self.roller_minutes.set_options("\n".join(['{:02d}'.format(hour) for hour in range(60)]), lv.roller.MODE.NORMAL)
        self.roller_minutes.set_visible_row_count(3)
        self.roller_minutes.set_style_border_width(0, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.roller_minutes.set_style_text_color(lv.color_white(), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.roller_minutes.set_style_bg_color(lv.color_black(), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.roller_minutes.set_style_bg_opa(lv.OPA.TRANSP, lv.PART.SELECTED | lv.STATE.DEFAULT)
        self.roller_minutes.set_style_pad_all(0, lv.PART.MAIN | lv.STATE.DEFAULT)

        self.roller_minutes.set_style_text_opa(lv.OPA.COVER, lv.PART.SELECTED | lv.STATE.DEFAULT)
        self.roller_minutes.set_style_text_opa(lv.OPA._80, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.roller_minutes.add_event_cb(
            lambda event: print('roller_minutes VALUE_CHANGED'),
            lv.EVENT.VALUE_CHANGED,
            None
        )
        self.sep2 = lv.label(self.layout)
        self.sep2.set_text(':')

        self.roller_seconds = lv.roller(self.layout)
        self.roller_seconds.set_options("\n".join(['{:02d}'.format(hour) for hour in range(60)]), lv.roller.MODE.NORMAL)
        self.roller_seconds.set_visible_row_count(3)
        self.roller_seconds.set_style_border_width(0, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.roller_seconds.set_style_text_color(lv.color_white(), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.roller_seconds.set_style_bg_color(lv.color_black(), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.roller_seconds.set_style_bg_opa(lv.OPA.TRANSP, lv.PART.SELECTED | lv.STATE.DEFAULT)
        self.roller_seconds.set_style_pad_all(0, lv.PART.MAIN | lv.STATE.DEFAULT)

        self.roller_seconds.set_style_text_opa(lv.OPA.COVER, lv.PART.SELECTED | lv.STATE.DEFAULT)
        self.roller_seconds.set_style_text_opa(lv.OPA._80, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.roller_seconds.add_event_cb(
            lambda event: print('roller_seconds VALUE_CHANGED'),
            lv.EVENT.VALUE_CHANGED,
            None
        )

        self.cancel = lv.btn(self.layout)
        self.cancel.set_size(100, 50)
        self.cancel_label = lv.label(self.cancel)
        self.cancel_label.set_text('取消')

        self.cancel.add_flag(lv.OBJ_FLAG_FLEX_IN_NEW.TRACK)
        self.cancel.set_style_text_color(lv.palette_main(lv.PALETTE.GREY), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.cancel.set_style_bg_opa(lv.OPA._30, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.cancel.set_style_bg_color(lv.palette_main(lv.PALETTE.GREY), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.cancel.add_event_cb(self.cancel_event_clicked_handler, lv.EVENT.CLICKED, None)

        self.ok = lv.btn(self.layout)
        self.ok.set_size(100, 50)
        self.ok.set_style_text_color(lv.palette_main(lv.PALETTE.BLUE), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ok.set_style_bg_opa(lv.OPA._30, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ok.set_style_bg_color(lv.palette_main(lv.PALETTE.YELLOW), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ok.add_event_cb(self.ok_event_clicked_handler, lv.EVENT.CLICKED, None)
        self.ok_label = lv.label(self.ok)
        self.ok_label.set_text('开始')

    def cancel_event_clicked_handler(self, event):
        print('{} cancel_event_clicked_handler'.format(type(self).__name__))

    def ok_event_clicked_handler(self, event):
        print('{} ok_event_clicked_handler'.format(type(self).__name__))


class CountDownScreen(Screen):
    NAME = 'countdownsetting_screen'

    def __init__(self):
        super().__init__()
        self.meta = lv.obj()
        self.meta.add_style(normal_style, lv.PART.MAIN | lv.STATE.DEFAULT)

        self.rt_img = lv.img(self.meta)
        self.rt_img.set_src('E:/media/chevron-left-y.png')
        self.rt_img.set_align(lv.ALIGN.TOP_LEFT)
        self.rt_label = lv.label(self.meta)
        self.rt_label.set_text('倒计时')
        self.rt_label.set_style_text_color(lv.palette_main(lv.PALETTE.YELLOW), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.rt_label.align_to(self.rt_img, lv.ALIGN.OUT_RIGHT_MID, 5, 0)

        self.time = lv.label(self.meta)
        self.time.set_text('09:00')
        self.time.set_align(lv.ALIGN.TOP_RIGHT)

        self.arc = lv.arc(self.meta)
        self.arc.set_size(200, 200)
        self.arc.set_range(0, 1000)
        self.arc.set_rotation(270)
        self.arc.set_bg_angles(0, 360)
        self.arc.set_style_arc_color(lv.palette_main(lv.PALETTE.ORANGE), lv.PART.INDICATOR | lv.STATE.DEFAULT)
        self.arc.center()
        self.arc.remove_style(None, lv.PART.KNOB)
        self.arc.clear_flag(lv.obj.FLAG.CLICKABLE)
        self.arc.set_value(1000)

        self.total = lv.label(self.arc)
        self.total.set_text('1分钟')
        self.total.align(lv.ALIGN.CENTER, 0, -40)

        self.remaining = lv.label(self.arc)
        self.remaining.set_text('01:00')
        self.remaining.align(lv.ALIGN.CENTER, 0, 0)

        self.cancel = lv.btn(self.meta)
        self.cancel_label = lv.label(self.cancel)
        self.cancel_label.set_text('取消')
        self.cancel.set_size(100, 50)
        self.cancel.set_style_align(lv.ALIGN.BOTTOM_LEFT, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.cancel.set_style_text_color(lv.palette_main(lv.PALETTE.GREY), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.cancel.set_style_bg_opa(lv.OPA._30, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.cancel.set_style_bg_color(lv.palette_main(lv.PALETTE.GREY), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.cancel.add_event_cb(self.cancel_event_clicked_handler, lv.EVENT.CLICKED, None)

        self.ok = lv.btn(self.meta)
        self.ok_label = lv.label(self.ok)
        self.ok_label.set_text('开始')
        self.ok.set_size(100, 50)
        self.ok.set_style_align(lv.ALIGN.BOTTOM_RIGHT, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ok.set_style_text_color(lv.palette_main(lv.PALETTE.BLUE), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ok.set_style_bg_opa(lv.OPA._30, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ok.set_style_bg_color(lv.palette_main(lv.PALETTE.YELLOW), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ok.add_event_cb(self.ok_event_clicked_handler, lv.EVENT.CLICKED, None)

        self.total_seconds = 60
        self.anim = None

    def cancel_event_clicked_handler(self, event):
        print('{} cancel_event_clicked_handler'.format(type(self).__name__))
        if self.anim:
            lv.anim_del_all()
            self.anim = None

    def ok_event_clicked_handler(self, event):
        print('{} ok_event_clicked_handler'.format(type(self).__name__))
        if self.anim:
            return
        self.anim = lv.anim()
        self.anim.set_var(self.arc)
        self.anim.set_values(1000, 0)
        self.anim.set_time(self.total_seconds * 1000)
        self.anim.set_custom_exec_cb(self.anim_custom_exec_cb)
        self.anim.set_ready_cb(self.anim_ready_cb)
        self.anim.start()

    def anim_custom_exec_cb(self, anim, value):
        self.arc.set_value(value)
        self.remaining.set_text('{:02d}:{:02d}'.format(int(value * 0.06) // 60, int(value * 0.06) % 60))

    def anim_ready_cb(self, anim):
        self.anim = None


class UI(Abstract):
    def __init__(self):
        self.screens = []
        self.current = None
        self.tileview_map = {
            "display_screen": [0, 0, lv.ANIM.OFF],
            "main_screen": [1, 0, lv.ANIM.OFF],
            "watch_face_screen": [2, 0, lv.ANIM.OFF],
            "app_list_1_screen": [3, 0, lv.ANIM.OFF],
            "app_list_2_screen": [4, 0, lv.ANIM.OFF],
            "heart_screen": [5, 0, lv.ANIM.OFF],
            "blood_screen": [6, 0, lv.ANIM.OFF],
            "temp_screen": [7, 0, lv.ANIM.OFF],
        }
        self.tileview_position_map = {
            (0, 0): "display_screen",
            (1, 0): "main_screen",
            (2, 0): "watch_face_screen",
            (3, 0): "app_list_1_screen",
            (4, 0): "app_list_2_screen",
            (5, 0): "heart_screen",
            (6, 0): "blood_screen",
            (7, 0): "temp_screen",
        }

    def lv_load(self, event, msg):
        for screen in self.screens:
            if screen.NAME == msg["screen"]:
                scr = screen
                if self.current != scr:
                    if self.current:
                        self.current.deactivate()
                        scr.last_screen_info = {"screen": self.current.NAME}
                    scr.set_prop(msg)
                    scr.post_processor_before_initialization()
                    scr.initialization()
                    scr.post_processor_after_initialization()
                    self.current = scr
                    if msg["screen"] in self.tileview_map:
                        lv.scr_load(tileview_screen)
                        tileview.set_tile_id(*self.tileview_map[msg['screen']])
                    else:
                        lv.scr_load(self.current.meta)

    def add_screen(self, screen):
        self.screens.append(screen)

    def post_processor_after_instantiation(self):
        for scr in self.screens:
            scr.post_processor_after_instantiation()
        EventMesh.subscribe("load_screen", self.lv_load)
        EventMesh.subscribe("load_tileview", self.lv_tileview)

    def lv_tileview(self, topic, msg):
        print(msg)
        screen = self.tileview_position_map[msg]
        EventMesh.publish("load_screen", {"screen": screen})

    def start(self):
        self.post_processor_after_instantiation()


