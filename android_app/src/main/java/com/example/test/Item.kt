package com.example.test

import java.io.Serializable

class Item(imgId: Int, text: String): Serializable {
    var imgId = imgId
    var text = text
}