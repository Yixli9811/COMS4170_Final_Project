function add_correct() {
    $.ajax({
        type: "POST",
        url: "../correct",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : "add",
        success: function(result){

        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}


let handleButton = function() {
    //handle submit..

    let answer = $('#answer').val()
    console.log(answer)

    answer = answer.toLowerCase()
    let correct = id.substring(1)

    $('#s1').addClass("hidden")
    $('#s2').addClass("hidden")
    $('#s3').removeClass("hidden")


    if(answer === correct) {
        $('#correct').removeClass("hidden")
        add_correct()
    }
    else {
        $('#incorrect').removeClass("hidden")
    }


}

function display_sales_list(sales) {
    $("#list").empty()

    let i = 0;
    console.log(sales)
    for(var sale of sales) {
        let row = $("<div>")
        row.addClass("row")

        let userDiv = $("<div>")
        let userInfo = $("<p>")
        userDiv.addClass("col-md-2")
        userInfo.text(sale.salesperson)

        let clientDiv = $("<div>")
        let clientInfo = $("<p>")
        clientDiv.addClass("col-md-4")
        clientInfo.text(sale.client)

        let amountDiv = $("<div>")
        let amountInfo = $("<p>")
        amountDiv.addClass("col-md-3")
        amountInfo.text(sale.reams)

        let deleteDiv = $("<div>")
        let deleteInfo = $("<button>")
        deleteDiv.addClass("col-md-3")
        deleteInfo.text("X")
        deleteInfo.attr('id', sale.id)
        deleteInfo.click(handleButton)

        userDiv.append(userInfo)
        clientDiv.append(clientInfo)
        amountDiv.append(amountInfo)
        deleteDiv.append(deleteInfo)

        row.append(userDiv)
        row.append(clientDiv)
        row.append(amountDiv)
        row.append(deleteDiv)

        row.draggable({revert: 'invalid'});
        row.attr('id', i)

        $("#list").append(row)
        i++;
    }
}

$(document).ready(function(){
    $('#quizBtn').addClass('active');
    $('#check').click(handleButton)
})

