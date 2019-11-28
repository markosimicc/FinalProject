package com.example.smartshelfapp;

import android.app.Activity;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;

import java.util.ArrayList;


public class AddPage extends Activity {

    EditText inputName;
    EditText inputPrice;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_add_page);
    }

    public void send (View v){
        ArrayList<String> text = new ArrayList<>();
        inputName = (EditText) findViewById(R.id.Name);
        inputPrice = (EditText) findViewById(R.id.Price);

        text.add(inputName.getText().toString());
        text.add((inputPrice.getText().toString()));

        MessageSender messageSender = new MessageSender();
        messageSender.execute(text);
    }
        }
