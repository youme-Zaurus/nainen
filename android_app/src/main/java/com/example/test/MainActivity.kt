package com.example.test

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.AdapterView
import android.widget.GridView

class MainActivity : AppCompatActivity() {

    // リストデータの取得
    var menu = mutableListOf<Item>()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        // GridViewオブジェクトを取得
        val gridLook = findViewById<GridView>(R.id.gridLook)
        // リストデータの追加
        menu.add(Item(R.drawable.scoups, "S.COUPS"))
        menu.add(Item(R.drawable.jeonghan, "JEONGHAN"))
        menu.add(Item(R.drawable.joshua, "JOSHUA"))
        menu.add(Item(R.drawable.jun, "JUN"))
        menu.add(Item(R.drawable.hoshi, "HOSHI"))
        menu.add(Item(R.drawable.wonwoo, "WONWOO"))
        menu.add(Item(R.drawable.woozi, "WOOZI"))
        menu.add(Item(R.drawable.the8, "THE 8"))
        menu.add(Item(R.drawable.mingyu, "MINGYU"))
        menu.add(Item(R.drawable.dk, "DK"))
        menu.add(Item(R.drawable.seungkwan, "SEUNGKWAN"))
        menu.add(Item(R.drawable.vernon, "VERNON"))
        menu.add(Item(R.drawable.dino, "DINO"))

        // ItemAdapterオブジェクトの作成
        var adapter = ItemAdapter(applicationContext, R.layout.column, menu)
        // GridViewオブジェクトにItemAdapterオブジェクトを設定
        gridLook.adapter = adapter

        // GridViewオブジェクトにリスナを登録
        gridLook.onItemClickListener = ListItemClickListener()
    }

    private inner class ListItemClickListener: AdapterView.OnItemClickListener {
        override fun onItemClick(parent: AdapterView<*>, view: View, pos: Int, id: Long) {
            // 選択した項目のデータを取得
            val item = parent.getItemAtPosition(pos) as Item
            // Intentオブジェクトの生成
            var intent = Intent(applicationContext, SubActivity::class.java)
            // Intentオブジェクトにデータを渡す
            intent.putExtra("item", item)
            // 2つめの画面を開く
            startActivity(intent)
        }
    }
}