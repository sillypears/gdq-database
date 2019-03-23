

function selectEvent (eventData) {
    var splitData = eventData.split(" ")
    var event = splitData[0]
    var year = splitData[1]

    var request = new XMLHttpRequest()

    request.open('GET', "api/" + event + "/" + year, true)
    request.onload = function() {
    // Begin accessing JSON data here
        var data = JSON.parse(this.response)
        
        tO = '<table class="table">'
        
        data.forEach(element => {
            tO = tO + "<tr>"
            tO = tO + "<td>"+element.Game+"</td>"
            tO = tO + "<td>"+element.Players+"</td>"
            tO = tO + "<td>"+element.Platform+"</td>"
            tO = tO + "<td>"+element.StartTime+"</td>"
            //tO = tO + "<td>"+element.Year+"</td>"
            tO = tO + "</tr>"
        });
        tO = tO + "</table>"
        $('#tableData').html(tO)
    }
    request.send()
}