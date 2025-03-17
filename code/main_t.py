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

from usr.common import *
from usr import EventMesh


class App(object):
    def __init__(self):
        self.managers = []

    def append_manager(self, manager):
        if isinstance(manager, Abstract):
            manager.post_processor_after_instantiation()
            self.managers.append(manager)
        return self

    def start(self):
        for manager in self.managers:
            manager.post_processor_before_initialization()
            manager.initialization()
            manager.post_processor_after_initialization()


class WearApp(App):
    def __init__(self):
        super(WearApp, self).__init__()
        self.__ui = None

    def set_ui(self, ui):
        self.__ui = ui

    def start(self):
        if self.__ui is not None:
            self.__ui.start()
        super().start()


# lcd 初始化在lcd.py中, 针对不同信号, 更换不懂的lcd驱动和触摸驱动
from usr import lcd
import uos

#挂载flash文件系统  
ldev = uos.VfsLfs1(32, 32, 32, "ext_fs", 0, 0)
uos.mount(ldev, '/ext')

# 穿戴应用初始化
wear = WearApp()

# 初始化ui, ui中有各个界面, 界面写好后加入到ui中, 界面的布局在css.py中, 针对静态的界面可以在以下生命周期中添加你需要实现的动态功能
# 创建界面的时候会执行post_processor_after_instantiation     只会执行一次在创建add_screen的时候
# 跳转到此页的时候会执行
    # post_processor_before_initialization
    # initialization
    # post_processor_after_initialization
# 离开此页的时候会执行
    # deactivate
from usr.ui import *

ui = UI()
ui.add_screen(MainScreen())
ui.add_screen(WatchFaceScreen())
ui.add_screen(AppList1Screen())
ui.add_screen(AppList2Screen())
ui.add_screen(DailScreen())
ui.add_screen(CallScreen())
ui.add_screen(BloodScreen())
ui.add_screen(TempScreen())
ui.add_screen(HeartScreen())

# 穿戴应用添加ui
wear.set_ui(ui)
# 穿戴应用添加后台处理器, 这里根据后台功能进行填充, ui订阅和发布获取manager中的数据, manager也可以主动投递给UI数据, 前提ui需要订阅TOPIC才能实现后台消息推送
from usr.mgr import *

wear.append_manager(DeviceManager())
# 启动应用
wear.start()

# 启动完成跳入主界面
EventMesh.publish("load_screen", {"screen": "main_screen"})
