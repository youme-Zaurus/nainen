package com.example.android_app.ui.userinfo

import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel

class UserinfoViewModel : ViewModel() {

    private val _text = MutableLiveData<String>().apply {
        value = "This is userinfo Fragment"
    }
    val text: LiveData<String> = _text
}