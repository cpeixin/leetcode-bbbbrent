/*
 * @version: 
 * @Author: Brent
 * @Date: 2023-01-05 22:09:57
 * @LastEditors: 
 * @LastEditTime: 2023-01-05 22:10:40
 * @Descripttion: 
 */
package MultiThread.geek.chatRoom;

import com.geekbang.chatroom.client.ChatRoomClient;

import java.io.IOException;

public class ChatRoomClientAppMain {
    public static void main(String[] args) throws IOException {
        String server = args[0];
        ChatRoomClient client = new ChatRoomClient(server);
        client.start();
    }
}
