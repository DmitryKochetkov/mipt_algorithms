from polygon_area import sortPointsClockwise, Vertex, shoelace

def equals(a: float, b: float):
    tol = 1e-09
    return abs(a-b) <= tol

def testTriangle():
    rightTriangle = [
        Vertex(0.0, 0.0), 
        Vertex(4.0, 0.0), 
        Vertex(0.0, 3.0)
    ]

    assert equals(shoelace(rightTriangle), 6.0)

    randomTriangle = [
        Vertex(0.4, 1), 
        Vertex(0.8, 2.2), 
        Vertex(3.6, 1.4)
    ]

    print(*sortPointsClockwise(randomTriangle))
    print(shoelace(randomTriangle))
    assert equals(shoelace(randomTriangle), 1.84)

def testRectangle():
    rectangle = [
        Vertex(-3.0, 5.0), 
        Vertex(6.0, -2.0),
        Vertex(0.0, -4.0),
        Vertex(3.0, 7.0)
    ]

    print(*sortPointsClockwise(rectangle))

    assert equals(shoelace(rectangle), 60.0)

def testSquare():
    square1 = [
        Vertex(0.0, 0.0),
        Vertex(2.0, 0.0),
        Vertex(2.0, 2.0),
        Vertex(0.0, 2.0)
    ]
    
    square2 = [
        Vertex(3.0, 3.0), 
        Vertex(5.0, 2.0), 
        Vertex(6.0, 4.0), 
        Vertex(4.0, 5.0)
    ]

    assert equals(shoelace(square1), 4.0)
    assert equals(shoelace(square2), 5.0)

def testQuadrangle():
    quadrangle = [
        Vertex(5.0, 11.0), 
        Vertex(12.0, 8.0), 
        Vertex(9.0, 5.0),
        Vertex(5.0, 6.0)
    ]

    assert equals(shoelace(quadrangle), 25.0)

def testPolygon():
    polygon = [
        Vertex(5.0, 11.0), 
        Vertex(12.0, 8.0), 
        Vertex(3.0, 4.0), 
        Vertex(9.0, 5.0),
        Vertex(5.0, 6.0)
    ]

    assert equals(shoelace(polygon), 30.0)
