class Solution(_w: Array[Int]) {
   
    //First add up all the weights and generate a totalWeight count
    val totalCount = _w.reduce((x,y) => x+y)
    val randomGenerator = scala.util.Random
   
    // Generates a random number between
    def generateRandomNumber(): Int = {
        val start = 1
        val end = totalCount
        start + randomGenerator.nextInt(end - start + 1)
    }

    def pickIndex(): Int = {
        val rand = generateRandomNumber
        println(s"rand: $rand")
        var curr = 0
        var pos = 0
        while(curr + _w(pos) < rand) {
            curr = curr + _w(pos)
            pos += 1
        }
        pos
    }

}
