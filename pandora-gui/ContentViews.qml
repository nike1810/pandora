import QtQuick 2.1
import QtQuick.Controls 1.0

Rectangle {
    id: rectangleViewes

    Row {
        id: mainRow
        anchors.fill: parent

        TableView {
            id: pandoraView
            model: tempPamdoraModel

            width: rectangleViewes.width / 2
            height: rectangleViewes.height

            TableViewColumn{ role: "artist"  ; title: "Artist" ; width: pandoraView.width / 3 }
            TableViewColumn{ role: "title"  ; title: "Title" ; width: pandoraView.width / 2 }
        }

        TableView {
            id: vkView
            model: tempVkModel

            width: rectangleViewes.width / 2
            height: rectangleViewes.height

            TableViewColumn{ role: "artist"  ; title: "Artist" ; width: vkView.width / 5 }
            TableViewColumn{ role: "title"  ; title: "Title" ; width: 2 * vkView.width / 5 }
            TableViewColumn{ role: "duration"  ; title: "Duration" ; width: vkView.width / 5 }
            TableViewColumn{ role: "quality"  ; title: "Quality" ; width: vkView.width / 5 }

        }

    }

    ListModel {
        id: tempPamdoraModel

        ListElement{ title: "A Masterpiece" ; artist: "Gabriel" }
        ListElement{ title: "Brilliance"    ; artist: "Jens" }
        ListElement{ title: "Outstanding"   ; artist: "Frederik" }
    }

    ListModel {
        id: tempVkModel

        ListElement{ title: "A Masterpiece" ; artist: "Gabriel"; duration: "3:00"; quality: "320"}
        ListElement{ title: "Brilliance"    ; artist: "Jens"; duration: "4:00"; quality: "128" }
        ListElement{ title: "Outstanding"   ; artist: "Frederik"; duration: "5:00"; quality: "192" }
    }
}

