# Copyright (c) Quectel Wireless Solution, Co., Ltd.All Rights Reserved.
 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
 
#     http://www.apache.org/licenses/LICENSE-2.0
 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import lvgl as lv


def lv_style_t(radius=None, bg_color=None, bg_grad_color=None, bg_grad_dir=None, bg_opa=None, border_width=None,
               border_opa=None, pad_left=None, pad_all=None, pad_gap=None, pad_right=None, pad_top=None,
               pad_bottom=None, img_recolor=None, shadow_width=None,
               img_recolor_opa=None, img_opa=None, line_color=None, line_width=None, line_rounded=None,
               shadow_color=None, shadow_opa=None, border_color=None, anim_speed=None, text_color=None, text_font=None,
               text_letter_space=None, pad_column=None, pad_row=None, layout=None, padding=None,
               flex_flow=None, main_place=None, cross_place=None, track_place=None, text_font_v2=None, bg_img_src=None):
    _style = lv.style_t()
    _style.init()
    if padding is not None:
        if len(padding) == 2:
            pad_top, pad_right, pad_bottom, pad_left = padding[0], padding[1], padding[0], padding[1]
        else:
            pad_top, pad_right, pad_bottom, pad_left = padding[0], padding[1], padding[2], padding[3]
    if bg_img_src is not None:
        _style.set_bg_img_src(bg_img_src)
    if text_font_v2 is not None:
        _style.set_text_font_v2(*text_font_v2)
    if flex_flow is not None:
        _style.set_flex_flow(flex_flow)
    if main_place is not None:
        _style.set_flex_main_place(main_place)
    if cross_place is not None:
        _style.set_flex_cross_place(cross_place)
    if track_place is not None:
        _style.set_flex_track_place(track_place)
    if layout is not None:
        _style.set_layout(layout)
    if pad_column is not None:
        _style.set_pad_column(pad_column)
    if pad_row is not None:
        _style.set_pad_row(pad_row)
    if radius is not None:
        _style.set_radius(radius)
    if bg_color is not None:
        _style.set_bg_color(bg_color)
    if bg_grad_color is not None:
        _style.set_bg_grad_color(bg_grad_color)
    if bg_grad_dir is not None:
        _style.set_bg_grad_dir(bg_grad_dir)
    if bg_opa is not None:
        _style.set_bg_opa(bg_opa)
    if border_width is not None:
        _style.set_border_width(border_width)
    if border_opa is not None:
        _style.set_border_opa(border_opa)
    if pad_left is not None:
        _style.set_pad_left(pad_left)
    if pad_right is not None:
        _style.set_pad_right(pad_right)
    if pad_top is not None:
        _style.set_pad_top(pad_top)
    if pad_bottom is not None:
        _style.set_pad_bottom(pad_bottom)
    if img_recolor is not None:
        _style.set_img_recolor(img_recolor)
    if img_recolor_opa is not None:
        _style.set_img_recolor_opa(img_recolor_opa)
    if img_opa is not None:
        _style.set_img_opa(img_opa)
    if line_color is not None:
        _style.set_line_color(line_color)
    if line_width is not None:
        _style.set_line_width(line_width)
    if line_rounded is not None:
        _style.set_line_rounded(line_rounded)
    if shadow_color is not None:
        _style.set_shadow_color(shadow_color)
    if shadow_opa is not None:
        _style.set_shadow_opa(shadow_opa)
    if border_color is not None:
        _style.set_border_color(border_color)
    if anim_speed is not None:
        _style.set_anim_speed(anim_speed)
    if text_color is not None:
        _style.set_text_color(text_color)
    if text_font is not None:
        _style.set_text_font(text_font)
    if text_letter_space is not None:
        _style.set_text_letter_space(text_letter_space)
    if pad_all is not None:
        _style.set_pad_all(pad_all)
    if pad_gap is not None:
        _style.set_pad_gap(pad_gap)
    if shadow_width is not None:
        _style.set_shadow_width(shadow_width)
    return _style


# create style style_scrollbar
style_scrollbar = lv_style_t(
    bg_opa=0
)
# style img
style_img = lv_style_t(
    img_opa=255
)
# line style
style_line = lv_style_t(
    bg_color=lv.color_hex(0x262626),
    bg_opa=lv.OPA.COVER
)
# 界面风格
screen_style = lv_style_t(
    bg_color=lv.color_hex(0x000000),
    bg_opa=255,
    pad_all=0,
    pad_gap=0
)
# 白
style_bg = lv_style_t(
    radius=0,
    img_recolor=lv.color_hex(0xffffff),
    img_recolor_opa=0,
    border_width=0,
    img_opa=255,
    pad_all=0
)
# 无色边框
style_btn = lv_style_t(
    shadow_width=0,
    border_width=0,
    bg_color=lv.color_hex(0x000000)
)

# flex布局
style_flex_row_wrap_between = lv_style_t(
    pad_column=0,
    pad_row=0,
    flex_flow=lv.FLEX_FLOW.ROW_WRAP,
    main_place=lv.FLEX_ALIGN.SPACE_BETWEEN,
    cross_place=lv.FLEX_ALIGN.SPACE_BETWEEN,
    track_place=lv.FLEX_ALIGN.SPACE_BETWEEN,
    layout=lv.LAYOUT_FLEX.value
)
# 14字体label样式
style_font_white_14 = lv_style_t(
    radius=0,
    bg_color=lv.color_hex(0x2195f6),
    bg_grad_color=lv.color_hex(0x2195f6),
    bg_grad_dir=lv.GRAD_DIR.VER,
    anim_speed=10,
    bg_opa=0,
    text_color=lv.color_hex(0xffffff),
    text_font_v2=("U:/14px.bin", 19),
    text_letter_space=0,
    pad_all=0
)
style_font_black_14 = lv_style_t(
    radius=0,
    bg_color=lv.color_hex(0x2195f6),
    bg_grad_color=lv.color_hex(0x2195f6),
    bg_grad_dir=lv.GRAD_DIR.VER,
    anim_speed=10,
    bg_opa=0,
    text_color=lv.color_hex(0x000000),
    text_font_v2=("U:/14px.bin", 19),
    text_letter_space=0,
    pad_all=0
)

# 宋体16字体label样式
style_font_16 = lv_style_t(
    radius=0,
    bg_color=lv.color_hex(0x2195f6),
    bg_grad_color=lv.color_hex(0x2195f6),
    bg_grad_dir=lv.GRAD_DIR.VER,
    anim_speed=10,
    bg_opa=0,
    text_color=lv.color_hex(0xffffff),
    text_font_v2=("U:/16px.bin", 19),
    text_letter_space=0,
    pad_all=0
)
style_font_20 = lv_style_t(
    radius=0,
    bg_color=lv.color_hex(0x2195f6),
    bg_grad_color=lv.color_hex(0x2195f6),
    bg_grad_dir=lv.GRAD_DIR.VER,
    anim_speed=10,
    bg_opa=0,
    text_color=lv.color_hex(0xffffff),
    text_font_v2=("U:/20px.bin", 23),
    text_letter_space=0,
    pad_all=0
)
style_font_28 = lv_style_t(
    radius=0,
    bg_color=lv.color_hex(0x2195f6),
    bg_grad_color=lv.color_hex(0x2195f6),
    bg_grad_dir=lv.GRAD_DIR.VER,
    anim_speed=10,
    bg_opa=0,
    text_color=lv.color_hex(0xffffff),
    text_font_v2=("U:/28px.bin", 33),
    text_letter_space=0,
    pad_all=0
)
style_font_56 = lv_style_t(
    radius=0,
    bg_color=lv.color_hex(0x2195f6),
    bg_grad_color=lv.color_hex(0x2195f6),
    bg_grad_dir=lv.GRAD_DIR.VER,
    anim_speed=10,
    bg_opa=0,
    text_color=lv.color_hex(0xffffff),
    text_font_v2=("U:/56px.bin", 66),
    text_letter_space=0,
    pad_all=0
)
style_font_black = lv_style_t(
    text_color=lv.color_hex(0x000000),
)
style_font_grey = lv_style_t(
    text_color=lv.color_hex(0x8c8c8c),
)
style_font_2094FA = lv_style_t(
    text_color=lv.color_hex(0x2094FA),
)
style_font_ffffff = lv_style_t(
    text_color=lv.color_hex(0xffffff),
)
style_font_ff5035= lv_style_t(
    text_color=lv.color_hex(0xff5035),
)
# 宋体20字体label样式
style_font_white_20 = lv_style_t(
    radius=0,
    bg_color=lv.color_hex(0x2195f6),
    bg_grad_color=lv.color_hex(0x2195f6),
    bg_grad_dir=lv.GRAD_DIR.VER,
    anim_speed=10,
    bg_opa=0,
    text_color=lv.color_hex(0xffffff),
    text_font_v2=("U:/20px.bin", 19),
    text_letter_space=0,
    pad_all=0
)
style_font_black_20 = lv_style_t(
    radius=0,
    bg_color=lv.color_hex(0x2195f6),
    bg_grad_color=lv.color_hex(0x2195f6),
    bg_grad_dir=lv.GRAD_DIR.VER,
    anim_speed=10,
    bg_opa=0,
    text_color=lv.color_hex(0x000000),
    text_font_v2=("U:/20px.bin", 19),
    text_letter_space=0,
    pad_all=0
)
# 宋体24字体label样式
style_font_white_24 = lv_style_t(
    radius=0,
    bg_color=lv.color_hex(0x2195f6),
    bg_grad_color=lv.color_hex(0x2195f6),
    bg_grad_dir=lv.GRAD_DIR.VER,
    anim_speed=10,
    bg_opa=0,
    text_color=lv.color_hex(0xffffff),
    text_font_v2=("U:/24px.bin", 19),
    text_letter_space=0,
    pad_all=0
)
style_font_black_24 = lv_style_t(
    radius=0,
    bg_color=lv.color_hex(0x2195f6),
    bg_grad_color=lv.color_hex(0x2195f6),
    bg_grad_dir=lv.GRAD_DIR.VER,
    anim_speed=10,
    bg_opa=0,
    text_color=lv.color_hex(0x000000),
    text_font_v2=("U:/24px.bin", 19),
    text_letter_space=0,
    pad_all=0
)
# 宋体28字体label样式
style_font_white_28 = lv_style_t(
    radius=0,
    bg_color=lv.color_hex(0x2195f6),
    bg_grad_color=lv.color_hex(0x2195f6),
    bg_grad_dir=lv.GRAD_DIR.VER,
    anim_speed=10,
    bg_opa=0,
    text_color=lv.color_hex(0xffffff),
    text_font_v2=("U:/28px.bin", 19),
    text_letter_space=0,
    pad_all=0
)
style_font_black_28 = lv_style_t(
    radius=0,
    bg_color=lv.color_hex(0x2195f6),
    bg_grad_color=lv.color_hex(0x2195f6),
    bg_grad_dir=lv.GRAD_DIR.VER,
    anim_speed=10,
    bg_opa=0,
    text_color=lv.color_hex(0x000000),
    text_font_v2=("U:/28px.bin", 19),
    text_letter_space=0,
    pad_all=0
)
# 宋体32字体label样式
style_font_white_32 = lv_style_t(
    radius=0,
    bg_color=lv.color_hex(0x2195f6),
    bg_grad_color=lv.color_hex(0x2195f6),
    bg_grad_dir=lv.GRAD_DIR.VER,
    anim_speed=10,
    bg_opa=0,
    text_color=lv.color_hex(0xffffff),
    text_font_v2=("U:/32px.bin", 19),
    text_letter_space=0,
    pad_all=0
)
style_font_black_32 = lv_style_t(
    radius=0,
    bg_color=lv.color_hex(0x2195f6),
    bg_grad_color=lv.color_hex(0x2195f6),
    bg_grad_dir=lv.GRAD_DIR.VER,
    anim_speed=10,
    bg_opa=0,
    text_color=lv.color_hex(0x000000),
    text_font_v2=("U:/32px.bin", 19),
    text_letter_space=0,
    pad_all=0
)
# 宋体40字体label样式
style_font_white_40 = lv_style_t(
    radius=0,
    bg_color=lv.color_hex(0x2195f6),
    bg_grad_color=lv.color_hex(0x2195f6),
    bg_grad_dir=lv.GRAD_DIR.VER,
    anim_speed=10,
    bg_opa=0,
    text_color=lv.color_hex(0xffffff),
    text_font_v2=("U:/40px.bin", 19),
    text_letter_space=0,
    pad_all=0
)
style_font_black_40 = lv_style_t(
    radius=0,
    bg_color=lv.color_hex(0x2195f6),
    bg_grad_color=lv.color_hex(0x2195f6),
    bg_grad_dir=lv.GRAD_DIR.VER,
    anim_speed=10,
    bg_opa=0,
    text_color=lv.color_hex(0x000000),
    text_font_v2=("U:/40px.bin", 19),
    text_letter_space=0,
    pad_all=0
)
# 宋体48字体label样式
style_font_white_48 = lv_style_t(
    radius=0,
    bg_color=lv.color_hex(0x2195f6),
    bg_grad_color=lv.color_hex(0x2195f6),
    bg_grad_dir=lv.GRAD_DIR.VER,
    anim_speed=10,
    bg_opa=0,
    text_color=lv.color_hex(0xffffff),
    text_font_v2=("U:/48px.bin", 19),
    text_letter_space=0,
    pad_all=0
)
style_font_black_48 = lv_style_t(
    radius=0,
    bg_color=lv.color_hex(0x2195f6),
    bg_grad_color=lv.color_hex(0x2195f6),
    bg_grad_dir=lv.GRAD_DIR.VER,
    anim_speed=10,
    bg_opa=0,
    text_color=lv.color_hex(0x000000),
    text_font_v2=("U:/48px.bin", 19),
    text_letter_space=0,
    pad_all=0
)

# 页眉容器样式
style_header = lv_style_t(
    radius=0,
    bg_color=lv.color_hex(0x000000),
    bg_grad_color=lv.color_hex(0x000000),
    bg_grad_dir=lv.GRAD_DIR.VER,
    bg_opa=0,
    border_color=lv.color_hex(0x000000),
    border_width=0,
    border_opa=255,
    pad_all=0
)
# 红圆
style_circle_max = lv_style_t(
    radius=lv.RADIUS.CIRCLE,
    shadow_width=0,
    border_width=0,
    anim_speed=10,
    bg_grad_dir=lv.GRAD_DIR.VER,
    pad_all=0
)
style_circle_22 = lv_style_t(
    radius=22,
    shadow_width=0,
    border_width=0,
    anim_speed=10,
    bg_grad_dir=lv.GRAD_DIR.VER,
    pad_all=0
)
# 黑色容器背景
style_cont = lv_style_t(
    radius=0,
    bg_color=lv.color_hex(0x000000),
    bg_grad_color=lv.color_hex(0x000000),
    anim_speed=10,
    bg_grad_dir=lv.GRAD_DIR.VER,
    bg_opa=0,
    border_width=0,
    pad_all=0
)
# create style style_list_scrollbar
style_list_scrollbar = lv_style_t(
    radius=3,
    bg_color=lv.color_hex(0x000000),
    bg_grad_color=lv.color_hex(0x000000),
    bg_grad_dir=lv.GRAD_DIR.VER,
    bg_opa=0
)
style_bg_opa_transp = lv_style_t(
    bg_opa=0
)
# 群组label 样式
style_group_label_black = lv_style_t(
    anim_speed=10
)

style_pad_default = lv_style_t(
    pad_all=0
)
style_gap_default = lv_style_t(
    pad_gap=0
)
style_flex_raw = lv_style_t(
    flex_flow=lv.FLEX_FLOW.ROW,
    main_place=lv.FLEX_ALIGN.START,
    cross_place=lv.FLEX_ALIGN.END,
    track_place=lv.FLEX_ALIGN.END,
    layout=lv.LAYOUT_FLEX.value
)
style_flex_raw_between = lv_style_t(
    flex_flow=lv.FLEX_FLOW.ROW,
    main_place=lv.FLEX_ALIGN.SPACE_BETWEEN,
    cross_place=lv.FLEX_ALIGN.END,
    track_place=lv.FLEX_ALIGN.END,
    layout=lv.LAYOUT_FLEX.value
)
style_flex_column_between = lv_style_t(
    flex_flow=lv.FLEX_FLOW.COLUMN,
    main_place=lv.FLEX_ALIGN.SPACE_BETWEEN,
    cross_place=lv.FLEX_ALIGN.END,
    track_place=lv.FLEX_ALIGN.END,
    layout=lv.LAYOUT_FLEX.value
)
style_img_signal = lv_style_t(
    bg_img_src="U:/media/s4.png"
)

style_img_gps = lv_style_t(
    bg_img_src="U:/media/point.png"
)
style_img_bat = lv_style_t(
    bg_img_src="U:/media/bat4.png"
)
# 主界面样式
style_main_screen = lv_style_t(
    bg_img_src="U:/media/20230913100558.png"
)
style_bar_top_main = lv_style_t(
    padding=[0, 12, 4, 12],
    pad_gap=0,
)
style_main_top_cont_1 = lv_style_t(
    pad_gap=4,
)
# watch_face页面样式
style_watch_face_bg = lv_style_t(
    bg_img_src="U:/media/r-b.png"
)

style_display_cont_1_cont_2 = lv_style_t(
    pad_left=8,
    pad_right=8
)
style_display_cont_2 = lv_style_t(
    radius=100,
    padding=[8, 12, 8, 12],
    pad_gap=8,
    border_width=1,
    border_color=lv.color_hex(0x262626)
)
style_app_list = lv_style_t(
    pad_left=6,
    pad_top=6,
    pad_gap=8
)
app_list2_cont = lv_style_t(
    pad_gap=16
)

style_bg_color_ff5035 = lv_style_t(
    bg_color=lv.color_hex(0xFF5035),
    bg_grad_color=lv.color_hex(0xFF5035)
)
style_bg_color_2094FA = lv_style_t(
    bg_color=lv.color_hex(0x2094FA),
    bg_grad_color=lv.color_hex(0x2094FA)
)
style_bg_color_42BF4B = lv_style_t(
    bg_color=lv.color_hex(0x42BF4B),
    bg_grad_color=lv.color_hex(0x42BF4B)
)
style_bg_color_FFB342 = lv_style_t(
    bg_color=lv.color_hex(0xFFB342),
    bg_grad_color=lv.color_hex(0xFFB342)
)
style_bg_color_262626 = lv_style_t(
    bg_color=lv.color_hex(0x262626),
    bg_grad_color=lv.color_hex(0x262626)
)
style_bg_color_FF352B = lv_style_t(
    bg_color=lv.color_hex(0xFF352B),
    bg_grad_color=lv.color_hex(0xFF352B)
)
style_dail_top = lv_style_t(
    pad_gap=0,
    padding=[0, 6, 6, 4]
)



