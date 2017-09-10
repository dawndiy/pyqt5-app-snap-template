import QtQuick 2.5
import Hello 1.0

Rectangle {
    width: 400
    height: 300

    Hello {
        id: hello
    }

    Text {
        anchors.centerIn: parent
        text: hello.text

        MouseArea {
            anchors.fill: parent
            onClicked: {
                hello.text = "Hello Ubuntu!"
            }
        }
    }
}
