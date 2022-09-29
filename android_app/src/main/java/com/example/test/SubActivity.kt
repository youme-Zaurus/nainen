package com.example.test

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.Button
import android.widget.ImageView
import android.widget.TextView

class SubActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_sub)

        // ボタンにリスナを設定
        val backButton = findViewById<Button>(R.id.backButton)
        val listener = ClickListener()
        backButton.setOnClickListener(listener)

        // ビューを取得
        val name = findViewById<TextView>(R.id.name)
        val member = findViewById<ImageView>(R.id.member)

        // Intentオブジェクトからデータを取り出す
        val item = intent.getSerializableExtra("item") as Item
        // ImageView, TextViewに表示
        member.setImageResource(item.imgId)
        name.text = item.text
    }

    inner class ClickListener: View.OnClickListener {
        override fun onClick(view: View) {
            if (view.id == R.id.backButton) {
                // この画面を閉じる
                finish()
            }
        }
    }
}