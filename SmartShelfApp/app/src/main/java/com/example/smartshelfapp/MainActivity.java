package com.example.smartshelfapp;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }


    public void openProductsOnShelf(View view){
        startActivity(new Intent(this, ProductsOnShelf.class));
    }

    public void openProductInfoSettings(View view){
        startActivity(new Intent(this,ProductInfoSettings.class));
    }

    public void openAddRemove(View view){
        startActivity(new Intent(this,AddRemove.class));
    }


}
