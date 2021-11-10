
function myFunc(){
    var field1=document.querySelector("#field1");
    if(field1.value!=""){
        field1.className="has-content";
    }else{
        field1.className="";
    }
    
}

function myFunc2(){
    var field2=document.querySelector("#field2");
    if(field2.value!=""){
        field2.className="has-content2";
    }else{
        field2.className="";
    }
}

myFunc();
myFunc2();