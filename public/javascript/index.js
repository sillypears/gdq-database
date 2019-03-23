

function selectEvent (eventData) {
    var splitData = eventData.split(" ")
    var event = splitData[0]
    var year = splitData[1]

    var request = new XMLHttpRequest()

    request.open('GET', "api/" + event + "/" + year, true)
    request.onload = function() {
    // Begin accessing JSON data here
        var data = JSON.parse(this.response)
        
        tO = '<table class="table table-striped table-hover table-sm table-responsive-sm">'
        tO = tO + '<thead class="thead-dark">'
        tO = tO + '<tr>'
        tO = tO + '<th scope="col">Game</th>'
        tO = tO + '<th scope="col">Runners</th>'
        tO = tO + '<th scope="col">Platform</th>'
        tO = tO + '<th scope="col">Start Time</th>'
        tO = tO + '</tr>'
        tO = tO + '</thead>'
        tO = tO + '<tbody>'
        data.forEach(element => {
            tO = tO + "<tr>"
            tO = tO + "<td scope=\"row\">"+element.Game+"</td>"
            tO = tO + "<td>"+element.Players+"</td>"
            tO = tO + "<td>"+element.Platform+"</td>"
            tO = tO + "<td>"+element.StartTime+"</td>"
            //tO = tO + "<td>"+element.Year+"</td>"
            tO = tO + "</tr>"
        });
        tO + tO + "</tbody>"
        tO = tO + "</table>"
        $('#tableData').html(tO)
    }
    request.send()
}