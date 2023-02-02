function solution(src) {
            var answer = src.substr(0,1);
            var before = src.substr(0,1);
            var cnt = 0;
            src.forEach((el, c) => {
                console.log(i);
                console.log(el);
                if(before == c) {
                    cnt++;
                }
                else{
                    before = c;
                    answer += (64 + cnt).charCodeAt(0);
                    cnt = 1;
                }
            })
            answer += (64 + cnt).charCodeAt(0);
            return answer;
        }
//        String src = "11111";
//        String src = "00011011100000";
    var src = "111100100011";
    console.log(solution(src))
    console.log("hi")