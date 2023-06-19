import io.StdIn.readLine

object laba3 extends App {
  val s = "бвгджзйклмнпрстфхцчшщ"; val g = "аеёиоуыэюя"
  val simb = readLine("Введите букву русского алфавита: ")
  if s.contains(simb.toLowerCase()) then println("Это согласная")
  else if g.contains(simb.toLowerCase()) then println("Это гласная")
  else println("Это не гласная и не согласная")
}



