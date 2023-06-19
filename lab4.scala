import scala.collection.mutable.ArrayBuffer, scala.io.StdIn.readInt

object lab4 extends App {

  def multip(A: ArrayBuffer[Int], B: ArrayBuffer[Int], N: Int): Unit =
    var P_A, P_B, P_S: Int = 1
    for i <- A do P_A *= i
    for j <- B do P_B *= j
    if P_B > 0 then println(P_A)
    else
      for i <- 0 until N do
        P_S *= (A(i)+B(i))
      print("Результат: " + P_S)

  print("N: "); val N: Int = readInt(); val A, B = new ArrayBuffer[Int](N); var n: Int = 0
  while n < N do
    print("Эл-т А: ")
    A += readInt(); n += 1
  while n > 0 do
    print("Эл-т В: ")
    B += readInt(); n -= 1

  multip(A, B, N)
}


