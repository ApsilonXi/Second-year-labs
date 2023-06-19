import io.StdIn._, math._

@main
def main(): Unit =
  print("Вход: ")
  val str = readLine()
  val S = figure(str)
  if S != 0.0 then print("Выход: " + S)

def figure(f: String): Double =
  f.split(" ").toList match
    case q@"Эллипс" :: _ :: _ :: Nil =>
      val r1 = q(1).toInt
      val r2 = q(2).toInt
      val S = r1*r2*Pi
      S
    case q@"Круг" :: _ :: Nil =>
      val r = q(1).toInt
      val S = r*r*Pi
      S
    case q@"Квадрат" :: _ :: Nil =>
      val a = q(1).toInt
      val S = a*a
      S
    case q@"Прямоугольник" :: _ :: _ :: Nil =>
      val a = q(1).toInt
      val b = q(2).toInt
      val S = a*b
      S
    case q@"Треугольник" :: _ :: _ :: Nil=>
      val a = q(1).toInt
      val h = q(2).toInt
      val S = 0.5*a*h
      S
    case _ =>
      println("Такая фигура не предусмотрена")
      0.0




