class Shape:
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        return "Drawing a Circle"
    
class Square(Shape):
    def draw(self):
        return "Drawing a Square"

class Factory:
    def create_shape(self, shape_type):
        if shape_type == "Circle":
            return Circle()
        elif shape_type == "Square":
            return Square()
        else:
            raise ValueError("Unknown shape type")
            

# Example usage
if __name == "__main__":
    factory = Factory()
    
    circle = factory.create_shape("Circle")
    print(circle.draw())  # Output: Drawing a Circle
    
    square = factory.create_shape("Square")
    print(square.draw())  # Output: Drawing a Square
    
    # Uncommenting the following line will raise a ValueError
    # unknown_shape = factory.create_shape("Triangle")
    # print(unknown_shape.draw())
