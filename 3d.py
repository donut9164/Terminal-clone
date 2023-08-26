import tkinter as tk
import math
import time

print("Running at")

class SpinningCubeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("3D Render")

        self.canvas = tk.Canvas(root, width=400, height=400)
        self.canvas.pack()

        self.cube_vertices = [
            (-50, -50, -50),
            (50, -50, -50),
            (50, 50, -50),
            (-50, 50, -50),
            (-50, -50, 50),
            (50, -50, 50),
            (50, 50, 50),
            (-50, 50, 50)
        ]

        self.cube_edges = [
            (0, 1), (1, 2), (2, 3), (3, 0),
            (4, 5), (5, 6), (6, 7), (7, 4),
            (0, 4), (1, 5), (2, 6), (3, 7)
        ]

        self.angle_x = 0
        self.angle_y = 0
        self.last_frame_time = time.time()  # Track time of last frame
        self.frames = 0  # Frame counter
        self.animate()

    def rotate_point(self, point, angle_x, angle_y):
        x, y, z = point

        cos_x = math.cos(angle_x)
        sin_x = math.sin(angle_x)
        cos_y = math.cos(angle_y)
        sin_y = math.sin(angle_y)

        new_x = x * cos_y - z * sin_y
        new_z = x * sin_y + z * cos_y

        final_x = new_x
        final_y = y * cos_x - new_z * sin_x
        final_z = y * sin_x + new_z * cos_x

        return final_x, final_y, final_z

    def project(self, point):
        x, y, z = point
        scale = 200 / (200 + z)  # Simple perspective projection
        screen_x = x * scale + 200
        screen_y = y * scale + 200
        return screen_x, screen_y

    def animate(self):
        start_time = time.time()

        self.canvas.delete("all")
        self.angle_x += 0.01
        self.angle_y += 0.01

        rotated_vertices = [self.rotate_point(vertex, self.angle_x, self.angle_y) for vertex in self.cube_vertices]
        projected_vertices = [self.project(vertex) for vertex in rotated_vertices]

        for edge in self.cube_edges:
            p1, p2 = edge
            x1, y1 = projected_vertices[p1]
            x2, y2 = projected_vertices[p2]
            self.canvas.create_line(x1, y1, x2, y2)

        end_time = time.time()
        frame_time = (end_time - start_time) * 1000  # Convert to milliseconds

        # Calculate FPS and display both FPS and average frame time
        self.frames += 1
        current_time = time.time()
        elapsed_time = current_time - self.last_frame_time
        if elapsed_time >= 1:  # Update FPS and average frame time every second
            fps = self.frames / elapsed_time
            avg_frame_time = elapsed_time / self.frames * 1000  # Average frame time in milliseconds
            print(f"\rFPS: {fps:.4f} - Avg Frame Time: {avg_frame_time:.6f} ms", end="")
            self.frames = 0
            self.last_frame_time = current_time

        self.root.after(10, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    app = SpinningCubeApp(root)
    root.mainloop()
