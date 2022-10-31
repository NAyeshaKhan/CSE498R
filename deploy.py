def main(img_path=None, vid_path=None, vid_out=None):
    print(f"[INFO] Loading model:")
    model=torch.hub.load('/yolov7-master', 'custom', source='local', path='best.pt', force_reload=True)
    
    classes=model.names
    
    #For detecting images
    if img_path!=None:
        print(f"[INFO] Working with image: {img_path}")
        img_out_name= f"./output/result_{img_path.split('/')[-1]}"
        
        frame=cv2.imread(img_path) #Reads the image
        frame=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        results= detectx(frame, model=model) #Detection occurs here
        
        frame=cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        frame= plot_boxes(results, frame, classes=classes)
        
        cv2.namedWindow("img_only", cv2.WINDOW_NORMAL) #Create a window to show results
        
        while True:
            cv2.imshow("img_only", frame)
            if cv2.waitKey(5) & 0xFF == ord('q'):
                print(f"[INFO] Exiting.")
                cv2.imwrite(f"{img_out_name}", frame)
                break
    elif vid_path!=None:
        print(f"Working with video: {vid_path}")
        cap=cv2.VideoCapture(vid_path)
        
        if vid_out:
            width= int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height= int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            fps= int(cap.get(cv2.CAP_PROP_FPS))
            codec= cv2.VideoWriter_fourcc(*'mp4v')
            out= cv2.VideoWriter(vid_out, codec, fps, (width, height))
        
        frame_no=1
        
        cv2.namedWindow("vid_out", cv2.WINDOW_NORMAL)
        while True:
            ret, frame= cap.read()
            if ret and frame_no %1 ==0:
                print(f"Working with frame: {frame_no}")
                
                frame= cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                results= detectx(frame, model=model)
                frame= cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
                
                frame.plot_boxes(results, frame, classes= classes)
                cv2.imshow("vid_out", frame)