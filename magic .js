function start(){
    document.getElementById('score').innerHTML="";
    let n=3;
    let one = parseInt(document.getElementById('one').value)
    let two = parseInt(document.getElementById('two').value)
    let three = parseInt(document.getElementById('three').value)
    let four = parseInt(document.getElementById('four').value)
    let five = parseInt(document.getElementById('five').value)
    let six = parseInt(document.getElementById('six').value)
    let seven = parseInt(document.getElementById('seven').value)
    let eight = parseInt(document.getElementById('eight').value)
    let nine = parseInt(document.getElementById('nine').value)

    let vars = [[one,two,three],[four,five,six],[seven,eight,nine]];
    //checking row sum
    let sum=15;
    let currsum=0;
    let flag=1;
    for(let i=0;i<3;i++){
        currsum =0;
        //checking row sum
        for(let j=0;j<n;j++){
            currsum+=vars[i][j];
        }
        if(currsum!=sum){
            flag=0;
            break;
        }
        currsum =0;
        //checking row sum
        if(flag)
        for(let j=0;j<n;j++){
            currsum+=vars[j][i];
        }
        if(currsum!=sum){
            flag=0;
            break;
        }
    }
    //checking diagonals
    if(flag){
        currsum=0;
        let dsum = vars[0][0] + vals[1][1] + vars[2][2];
        if(dsum!=sum)
            flag=0;
        if(flag)
        {
            dsum = vars[0][2] + vars[1][1] +vars[2][0];
            if(dsum!=sum)
            flag=0;
        }
    }
    var h1 = document.createElement('h1');
    h1.setAttribute('id','result')
    if(flag){
        console.log("won");
        h1.setAttribute("class",'won')
        var textNode= document.createTextNode("You Won!!!");
    }else{
            console.log("lost")
            var textNode= document.createTextNode("You Lost!!!");
            h1.setAttribute("class",'lost')
    }
    h1.appendChild(textNode)
    document.getElementById('score').appendChild(h1);
}