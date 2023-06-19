object lab5_2 extends App {
  type Set = Int => Boolean
  def singletonSet(elem: Int): Set = x => x == elem
  def union(a: Set, b: Set): Set = x => a(x) || b(x)
  def intersect(a: Set, b: Set): Set = x => a(x) && b(x)
  def diff(a: Set, b: Set): Set = x => a(x) && !b(x)
  def filter(s: Set, p: Int => Boolean): Set = intersect(s, p)

}
