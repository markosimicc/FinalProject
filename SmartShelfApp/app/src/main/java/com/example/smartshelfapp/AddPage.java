package com.example.smartshelfapp;

import android.app.Activity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;


public class AddPage extends Activity {

    EditText inputName;
    Button buttonSend;
    //EditText Price;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_add_page);
        //Price = (EditText) findViewById(R.id.Price);
    }

    public void send (View v){

        inputName = (EditText) findViewById(R.id.Name);
        //buttonSend = (Button)findViewById(R.id.send);

        MessageSender messageSender = new MessageSender();
        messageSender.execute(inputName.getText().toString());
    }

        }
