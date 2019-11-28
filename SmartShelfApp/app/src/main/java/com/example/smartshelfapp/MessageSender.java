package com.example.smartshelfapp;

import android.os.AsyncTask;

import java.io.IOException;
import java.io.PrintWriter;
import java.net.Socket;
import java.util.ArrayList;

public class MessageSender extends AsyncTask <ArrayList,Void,Void> {
    Socket socket;
    PrintWriter pw;


    @Override
    protected Void doInBackground(ArrayList... voids) {
        ArrayList <String> list = voids[0];
        System.out.println(list);
        try {
            socket = new Socket("172.17.93.35", 7800);
            pw = new PrintWriter(socket.getOutputStream());
            pw.write(list.get(0) + " "+ list.get(1));
            pw.flush();
            pw.close();
            socket.close();

        } catch (IOException e) {
            e.printStackTrace();
        }
        return null;
    }
}
