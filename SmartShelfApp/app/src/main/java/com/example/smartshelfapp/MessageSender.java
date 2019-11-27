package com.example.smartshelfapp;

import android.os.AsyncTask;

import java.io.IOException;
import java.io.PrintWriter;
import java.net.Socket;

public class MessageSender extends AsyncTask <String,Void,Void> {
    Socket socket;
    PrintWriter pw;

    @Override
    protected Void doInBackground(String... voids) {
        String message = voids[0];
        try {
            socket = new Socket("172.17.73.103", 5050);
            pw = new PrintWriter(socket.getOutputStream());
            pw.write(message);
            pw.flush();
            pw.close();
            socket.close();

        } catch (IOException e) {
            e.printStackTrace();
        }
        return null;
    }
}
