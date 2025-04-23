from memory import memset_zero, UnsafePointer
alias type = DType.int32

struct Matrix[rows: Int, cols: Int]:
    var data: UnsafePointer[Scalar[type]]

    # Initialize zeroeing all values
    fn __init__(out self):
        self.data = UnsafePointer[Scalar[type]].alloc(rows * cols)
        memset_zero(self.data, rows * cols)

    # Initialize taking a pointer, don't set any elements
    fn __init__(out self, data: UnsafePointer[Scalar[type]]):
        self.data = data

    # Initialize with random values
    @staticmethod
    fn rand() -> Self:
        var data = UnsafePointer[Scalar[type]].alloc(rows * cols)
        rand(data.address, rows * cols)
        return Self(data)

    fn __getitem__(self, y: Int, x: Int) -> Scalar[type]:
        return self.load[1](y, x)

    fn __setitem__(self, y: Int, x: Int, val: Scalar[type]):
        self.store(y, x, val)

    fn load[nelts: Int](self, y: Int, x: Int) -> SIMD[type, nelts]:
        return self.data.load[width=nelts](y * self.cols + x)

    fn store[nelts: Int, //](self, y: Int, x: Int, val: SIMD[type, nelts]):
        return self.data.store(y * self.cols + x, val)