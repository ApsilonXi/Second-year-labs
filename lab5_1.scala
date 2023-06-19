import collection.mutable.ArrayBuffer
object lab5_1 extends App {
  def program(clo: () => Int): Unit =
    var x = clo()
    while x != 0 do
      println(x)
      x = clo()

  def clo(n: Int): () => Int =
    var arr = new ArrayBuffer[Int](n)
    def rand(): Int =
        val x = 1 + util.Random.nextInt(n)
        x match
          case y if arr.contains(y) == false =>
            arr += y
            y
          case y if arr.length == n => 0
          case y => rand()
    rand

  print("N: ")
  val N = io.StdIn.readInt()
  program(clo(N))

}