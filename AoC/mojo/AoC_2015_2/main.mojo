
@value
struct Box():
    var l: Int
    var w: Int
    var h: Int

    fn __init__(out self, l: String, w: String, h: String) raises:
        try:
            self.l = int(l)
            self.w = int(w)
            self.h = int(h)
        except e:
            print("Exception (nill box created): ", e)
            self.l = 0
            self.w = 0
            self.h = 0

    fn asString(self) -> String:
        return str(self.l) + "x" + str(self.w) + "x" + str(self.h)

    fn surfaceArea(self) -> Int:
        var area = 2*self.l*self.w + 2*self.w*self.h + 2*self.h*self.l
        return area + min(self.h*self.l, min(self.l*self.w, self.w*self.h))

fn area(measures: List[String]) raises -> Int:
    l = int(measures[0])
    w = int(measures[1])
    h = int(measures[2])
    var area: Int = 2*l*w + 2*w*h + 2*h*l
    return area + min(h*l, min(l*w, w*h))

def makeBox(s: String):
    ...

def main():

    var f: FileHandle = open("input.txt", "r")
    lines = f.read()
    f.close()

    var text: List[String] = lines.split("\n")[:-1]
    var measures: List[String]

    var acc: Int = 0
    for i in range(len(text)):
        measures = text[i].split("x")
        #acc += Box(measures[0],measures[1],measures[2]).surfaceArea()
        acc += area(measures)


    print(acc)
