import io.StdIn.readInt

@main
def game(): Unit = {
  val R: Int = 94
  println("Введите число: ")
  var num: Int = readInt()
  var f: Int = 1
  while (f == 1) {
    if (num > R) {
      println("Ваше число больше.")
      num = readInt()
    }
    if (num < R) {
      println("Ваше число меньше.")
      num = readInt()
    }
    else {
      println("Вы угадали!")
      f += 1
    }
  }
}





