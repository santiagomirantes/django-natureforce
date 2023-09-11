/* ELEMENTS */

let receivedTitle = document.querySelector("#choosen")
let sentTitle = document.querySelector("h3:not(#choosen)")
let received = document.querySelector("#received")
let sent = document.querySelector("#sent")

function change(mode) {
    if(mode === "sent") {
      receivedTitle.removeAttribute("id")
      sentTitle.setAttribute("id","choosen")
      received.style.display = "none"
      sent.style.display = "unset"
    }
    else {
        receivedTitle.setAttribute("id", "choosen")
        sentTitle.removeAttribute("id")
        received.style.display = "unset"
        sent.style.display = "none"
      }
}

change("received")