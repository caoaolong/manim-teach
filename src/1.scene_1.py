from manim import *

class SceneTest1(Scene):
    def construct(self):
        circle = Circle()
        # play会自动添加对象, 因此add函数可以省略
        # self.add(circle)
        self.play(Create(circle))
        # 暂停0.5秒
        self.pause(duration=0.5)
        # 删除元素
        self.remove(circle)
        # 再次播放
        self.play(Create(circle))
        # 清空场景
        self.clear()
        # 等待0.5秒
        self.wait(duration=0.5)