object lab5_3 extends App {
  type Set = Int => Boolean
  val num = 1000
  def contains(s: Set, elem: Int): Boolean = s(elem)
  def forall(s: Set, p: Int => Boolean): Boolean =
    def view(a: Int): Boolean =
      if (a > num) then true
      else if (contains(s, a) && !p(a)) then false
      else view(a + 1)
    view(-num)
  def exists(s: Set, p: Int => Boolean): Boolean = !forall(s, (x => !p(x)))
  def map(s: Set, f: Int => Int): Set = (x => exists(s, (y: Int) => f(y) == x))
}
