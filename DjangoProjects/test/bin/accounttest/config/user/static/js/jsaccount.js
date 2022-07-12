var list = [];

function get_inform() {
    var obj = {};
    obj.id = $('#user_ID').val();
    obj.password = $('#user_PW1').val();
    obj.name = $('#user_name').val();
    var birth;
    var year = document.getElementById("year");
    
    year = year.options[year.selectedIndex].value;
    var month = document.getElementById("month");
    month = month.options[month.selectedIndex].value;
    target = document.getElementById("day");
    birth += target.options[target.selectedIndex].value;
    alert(birth);
    obj.gender = $('input[name=gender]:checked').val();
    obj.email = document.getElementsByName('user_email').value;
    obj.phonenum = document.getElementsByName('user_phone').value;

    str = JSON.stringify(obj);
    alert(str);
    var temp = "회원가입 정보\n\n" + "ID : " + obj.id + "\npassword : " + obj.password + "\n이름 : " + obj.name;
    alert(temp);
    list.push(str);

}


