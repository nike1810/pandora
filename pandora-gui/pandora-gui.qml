import QtQuick 2.1
import QtQuick.Controls 1.0
import QtQuick.Window 2.0


ApplicationWindow {
    id: root
//    title: qsTr("Hello World")
    width: 640
    height: 480

    Item {
        id: rootItem
        anchors.fill: parent

        Rectangle {
            id: pandoraSettings
            width: parent.width / 2
            height: parent.height / 4
            anchors.top : parent.top
            anchors.left: parent.left
            border.width: 1
            border.color: "#c0c0c0"

            Grid {
                id: pandoraGrid
                columns: 2
                rows: 2
                spacing: 10
                anchors.centerIn: parent

                anchors.leftMargin: 50
                anchors.rightMargin: 50

                horizontalItemAlignment: Grid.AlignHCenter
                verticalItemAlignment: Grid.AlignVCenter


                Label {
                    text: qsTr("Login:")
                    horizontalAlignment: Text.AlignLeft
                    width: pandoraSettings.width / 2 - 2 * parent.spacing - pandoraGrid.anchors.leftMargin
                }
                TextField {
                    width: pandoraSettings.width / 2 - 2 * parent.spacing - pandoraGrid.anchors.rightMargin

                }
                Label {
                    text: qsTr("Count:")
                    horizontalAlignment: Text.AlignLeft
                    width: pandoraSettings.width / 2 - 2 * parent.spacing - pandoraGrid.anchors.leftMargin
                }
                TextField {
                    width: 2 * pandoraSettings.width / 5 - 2 * parent.spacing - pandoraGrid.anchors.rightMargin

                }
            }

        }

        Rectangle {
            id: vkSettings
            width: parent.width / 2
            height: parent.height / 4
            anchors.top : parent.top
            anchors.right: parent.right
            border.width: 1
            border.color: "#c0c0c0"

            Grid {
                id: vkGrid
                columns: 2
                rows: 2
                spacing: 10
                anchors.centerIn: parent

                anchors.leftMargin: 50
                anchors.rightMargin: 50

                horizontalItemAlignment: Grid.AlignHCenter
                verticalItemAlignment: Grid.AlignVCenter


                Label {
                    text: qsTr("Login:")
                    horizontalAlignment: Text.AlignLeft
                    width: vkSettings.width / 2 - 2 * parent.spacing - vkGrid.anchors.leftMargin
                }
                TextField {
                    width: vkSettings.width / 2 - 2 * parent.spacing -vkGrid.anchors.rightMargin

                }
                Label {
                    text: qsTr("Password:")
                    horizontalAlignment: Text.AlignLeft
                    width: vkSettings.width / 2 - 2 * parent.spacing - vkGrid.anchors.leftMargin
                }
                TextField {
                    width: vkSettings.width / 2 - 2 * parent.spacing - vkGrid.anchors.rightMargin

                }
            }

        }

        ContentViews {
            id: contentViews
            anchors.top: pandoraSettings.bottom
            anchors.bottom: parent.bottom
            anchors.left: parent.left
            anchors.right: parent.right
        }
    }

//    Rectangle {
//        id: pandoraSettings
//        width: parent.width / 2
//        height: parent.height / 4
//        anchors.top : parent.top
//        anchors.left: parent.left

//    }

//    ContentViews {
//        id: contentViews
//        anchors.top: pandoraSettings.bottom
//        anchors.bottom: parent.bottom
//        anchors.left: parent.
//    }

//    Rectangle {
//        id: rectangleViewes
//        anchors.fill: parent

//        Row {
//            id: mainRow
//            anchors.fill: parent

//            TableView {
//                id: pandoraView
//                model: tempPamdoraModel

//                width: rectangleViewes.width / 2
//                height: rectangleViewes.height

//                TableViewColumn{ role: "artist"  ; title: "Artist" ; width: pandoraView.width / 3 }
//                TableViewColumn{ role: "title"  ; title: "Title" ; width: pandoraView.width / 2 }
//            }

//            TableView {
//                id: vkView
//                model: tempVkModel

//                width: rectangleViewes.width / 2
//                height: rectangleViewes.height

//                TableViewColumn{ role: "artist"  ; title: "Artist" ; width: vkView.width / 5 }
//                TableViewColumn{ role: "title"  ; title: "Title" ; width: 2 * vkView.width / 5 }
//                TableViewColumn{ role: "duration"  ; title: "Duration" ; width: vkView.width / 5 }
//                TableViewColumn{ role: "quality"  ; title: "Quality" ; width: vkView.width / 5 }

//            }

//        }

//        ListModel {
//            id: tempPamdoraModel

//            ListElement{ title: "A Masterpiece" ; artist: "Gabriel" }
//            ListElement{ title: "Brilliance"    ; artist: "Jens" }
//            ListElement{ title: "Outstanding"   ; artist: "Frederik" }
//        }

//        ListModel {
//            id: tempVkModel

//            ListElement{ title: "A Masterpiece" ; artist: "Gabriel"; duration: "3:00"; quality: "320"}
//            ListElement{ title: "Brilliance"    ; artist: "Jens"; duration: "4:00"; quality: "128" }
//            ListElement{ title: "Outstanding"   ; artist: "Frederik"; duration: "5:00"; quality: "192" }
//        }
//    }
    
//    menuBar: MenuBar {
//        Menu {
//            title: qsTr("File")
//            MenuItem {
//                text: qsTr("Exit")
//                onTriggered: Qt.quit();
//            }
//        }
//    }
    
//    Button {
//        text: qsTr("Hello World")
//        anchors.horizontalCenter: parent.horizontalCenter
//        anchors.verticalCenter: parent.verticalCenter
//    }
}
