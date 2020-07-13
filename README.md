# Immune-Kit-Development
This is made for people who do not want to edit the mod code, or don't know how to.
All you have to do is run the program, follow the steps, copy all the code it gives you (from top to bottom) and put it into one document. Then you open the MyMod folder in the SRC of ImmuneCommandMod. Then open chatcommandextensions in VS. Now copy the code from the document you made and paste it in after the 
internal static void HandleChatCommand(string text, ServerPlayer player, NetIncomingMessage msg)
        {
            var server = (LidServer)UnityEngine.Object.FindObjectOfType(typeof(LidServer));
            string[] commands = text.Split(' ');
            switch (commands[0])
            {
            
             HERE
Then paste it where it says here. Then upload it to the server and your done!
