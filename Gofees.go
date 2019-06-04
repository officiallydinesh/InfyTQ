//PF-Exer-8
//This verification is based on string match.

package main
import ("fmt")
func main(){
    var finalFee float64
    //Write your program logic here
    //Populate the variable: finalFee
var coursefee float64=25000
var extrafees float64=1500
var discount float64
discount=70/2 
discount=discount/float64(100) 
discount=discount*coursefee
//fmt.Println(discount)

finalFee=(coursefee-discount)+extrafees

     //Do not modify the below print statement for verification to work
     fmt.Println(finalFee) 
}
