package com.example.android_app

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.Button
import android.widget.Toast

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val loginButton = findViewById<Button>(R.id.login_button)
        val listener = ClickListener()
        loginButton.setOnClickListener(listener)

        val registerButton = findViewById<Button>(R.id.register_button)
        registerButton.setOnClickListener(listener)
    }
    private inner class ClickListener: View.OnClickListener {
        override fun onClick(view: View) {
            if(view.id == R.id.login_button) {
                Toast.makeText(applicationContext, "ログインボタン", Toast.LENGTH_SHORT).show()
            }
            else if(view.id == R.id.register_button) {
                Toast.makeText(applicationContext, "新規登録ボタン", Toast.LENGTH_SHORT).show()
            }
        }
    }
}