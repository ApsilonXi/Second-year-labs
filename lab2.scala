import io.StdIn.readInt, scala.collection.mutable.ArrayBuffer

@main
def matrix(): Unit =
  print("M: "); val rows: Int = readInt()
  print("N: "); val columns: Int = readInt()
  val Matrix = Array.ofDim[Int](rows, columns); val MatrixNew = ArrayBuffer[Int]()
  println("Значения: ")
  for i <- 0 until rows do
    for j <- 0 until columns do
      Matrix(i)(j) = readInt()

  for i <- 0 until rows do
    for j <- 0 until columns do
      print(Matrix(i)(j)+" ")
    println()

  println("Строка для удаления: "); val del_r: Int = readInt()
  println("Столбец для удаления: "); val del_c: Int = readInt()
  if del_r > rows then println("Такой строки нет")
  else if del_c > columns then println("Такого столбца нет")
  else if del_r <= rows & del_c <= columns then
    for i <- 0 until rows do
      for j <- 0 until columns do
        if i != del_r-1 & j != del_c-1 then MatrixNew += Matrix(i)(j)

  for i <- MatrixNew.indices do print(MatrixNew(i) + " ")










