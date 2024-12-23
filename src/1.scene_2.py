from manim import *

class SceneTest2(Scene):
    def construct(self):
        # 1. 创建一些 Mobjects
        circle = Circle(color=BLUE, fill_opacity=0.8).shift(LEFT / 2)
        square = Square(color=GREEN, fill_opacity=0.8).shift(RIGHT / 2)
        triangle = Triangle(color=YELLOW, fill_opacity=0.8).shift(UP / 2)

        # 2. 使用 add 添加元素到场景
        self.add(circle, square)
        self.wait(1)  # 场景显示圆和方形

        # 3. 添加单个元素到前景
        self.add_foreground_mobject(triangle)
        self.wait(1)  # 三角形在最前面显示

        # 4. 添加多个元素到前景
        self.add_foreground_mobjects(circle, square)
        self.wait(1)  # 圆和方形移动到前景

        # 5. 从前景移除一个元素
        self.remove_foreground_mobject(square)
        self.wait(1)  # 方形回到背景

        # 6. 从前景移除多个元素
        self.remove_foreground_mobjects(circle, triangle)
        self.wait(1)  # 圆和三角形回到背景

        # 7. 获取场景中顶级元素和所有子元素
        top_level_mobjects = self.get_top_level_mobjects()
        all_family_members = self.get_mobject_family_members()
        print(f"Top-level mobjects: {top_level_mobjects}")
        print(f"All family members: {all_family_members}")

        # 8. 动画中移除一个元素
        self.remove(circle)
        self.wait(1)  # 圆从场景中移除

        # 9. 清空场景
        self.clear()
        self.wait(1)  # 场景清空