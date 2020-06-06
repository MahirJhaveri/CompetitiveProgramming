// 39. Combination Sum

object Solution {
   
    // Get list of combinations that sum to target stating from position start
    def combinationSumAux(candidates: Array[Int], target: Int, start: Int): List[List[Int]] = {
        if (start >= candidates.length) {
            List[List[Int]]()
        }
        else if(start == candidates.length-1) {
            if (target % candidates(start) == 0) {
                //println("HAHAHAH")
                var new_lst = List[Int]()
                var i = 0
                while (target-candidates(start)*i > 0) {
                    new_lst = candidates(start) :: new_lst
                    i += 1
                }
                List[List[Int]](new_lst)
            } else {
                List[List[Int]]()
            }
        } else {
            var result = List[List[Int]]()
            var multiplier = 0
            while (target-candidates(start)*multiplier > 0) {
                var tmp = combinationSumAux(candidates, target-candidates(start)*multiplier, start+1)
                for(lst <- tmp) {
                    var new_lst = lst
                    var i = 0
                    while (i < multiplier) {
                        new_lst = candidates(start) :: new_lst
                        i += 1
                    }
                    result = new_lst :: result
                }
                multiplier += 1
            }
            if (candidates(start)*multiplier == target) {
                var new_lst = List[Int]()
                var i = 0
                while (i < multiplier) {
                    new_lst = candidates(start) :: new_lst
                    i += 1
                }
                result = new_lst :: result
            }
            result
        }
    }
   
    def combinationSum(candidates: Array[Int], target: Int): List[List[Int]] = {
        if (candidates.length == 0) {
            List[List[Int]]()
        } else {
            combinationSumAux(candidates, target, 0)
        }
    }
}
