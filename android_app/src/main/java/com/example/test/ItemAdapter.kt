package com.example.test

import android.content.Context
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.BaseAdapter
import android.widget.ImageView
import android.widget.TextView

class ItemAdapter(context: Context, layoutId: Int, items: List<Item>): BaseAdapter() {
    private val layoutInflater = context.getSystemService(Context.LAYOUT_INFLATER_SERVICE) as LayoutInflater
    val layoutId = layoutId
    val items = items

    override fun getCount(): Int {
        return items.count()
    }

    override fun getItem(pos: Int): Any {
        return items[pos]
    }

    override fun getItemId(pos: Int): Long {
        return pos.toLong()
    }

    override fun getView(pos: Int, convertView: View?, parent: ViewGroup?): View {
        // viewの作成
        val view = layoutInflater.inflate(layoutId, parent, false)
        // ImageViewを取得
        var img = view.findViewById<ImageView>(R.id.icon)
        // TextViewを取得
        var title = view.findViewById<TextView>(R.id.title)
        // ImageViewに画像を設定
        img.setImageResource(items[pos].imgId)
        // TextViewにテキストを設定
        title.text = items[pos].text

        return view
    }
}