import {useEffect, useState} from 'react';
import "./uploader.scss";
import {Button} from "@mui/material";
import axios from 'axios';

const Uploader = () => {

  const [image, setImage] = useState({
    image_file: "",
    preview_URL: require('./123.png'),
  });

  const nope=require("./123.png");

  const [image2, setImage2] = useState(require('./123.png'));
  const [image3, setImage3] = useState(require('./123.png'));
  const [image4, setImage4] = useState(require('./123.png'));
  const [image5, setImage5] = useState(require('./123.png'));


  const [text2, setText2] = useState('출력이미지');
  const [text3, setText3] = useState('출력이미지');
  const [text4, setText4] = useState('출력이미지');
  const [text5, setText5] = useState('출력이미지');


  const alpaca=require("./alpaca.jpg");
  const bear=require("./bear.jpg");
  const cat=require("./cat.png");
  const dog=require("./dog.jpeg");
  const fox=require("./fox.jpg");
  const horse=require("./horse.jpg");
  const mouse=require("./mouse.jpg");
  const panda=require("./panda.jpg");


  let inputRef;

  const saveImage = (e) => {
    e.preventDefault();
    if(e.target.files[0]){
      // 새로운 이미지를 올리면 createObjectURL()을 통해 생성한 기존 URL을 폐기
      URL.revokeObjectURL(image.preview_URL);
      const preview_URL = URL.createObjectURL(e.target.files[0]);
      setImage(() => (
        {
          image_file: e.target.files[0],
          preview_URL: preview_URL
        }
      ))
    }
  }

  const deleteImage = () => {
    // createObjectURL()을 통해 생성한 기존 URL을 폐기
    URL.revokeObjectURL(image.preview_URL);
    setImage({
      image_file: "",
      preview_URL: nope,
    });
    setImage2(nope);
    setImage3(nope);
    setImage4(nope);
    setImage5(nope);
    setText2('출력이미지');
    setText3('출력이미지');
    setText4('출력이미지');
    setText5('출력이미지');
  }

  useEffect(()=> {
    // 컴포넌트가 언마운트되면 createObjectURL()을 통해 생성한 기존 URL을 폐기
    return () => {
      URL.revokeObjectURL(image.preview_URL)
    }
  }, [])

  const sendImageToServer = async () => {
    if (image.image_file) {
      const formData = new FormData();
      formData.append('file', image.image_file);
      await axios({
        method:"post",
        url:'http://localhost:5000/',
        data:formData,
      })
      .then((res) => {
        console.log(res.data);
        for(var i=0;i<4;i++)
        {
          var kind=res.data[i][0];
          var per=String(res.data[i][1]);
          var temp=nope;
          if(kind=="alpaca")
          {
            temp=alpaca;
          }
          else if(kind=="bear")
          {
            temp=bear;
          }
          else if(kind=="cat")
          {
            temp=cat;
          }
          else if(kind=="dog")
          {
            temp=dog;
          }
          else if(kind=="fox")
          {
            temp=fox;
          }
          else if(kind=="horse")
          {
            temp=horse;
          }
          else if(kind=="mouse")
          {
            temp=mouse;
          }
          else if(kind=="panda")
          {
            temp=panda;
          }
          if(i==0)
          {
            setImage2(temp);
            setText2(kind+" "+per+"%");
          }
          else if(i==1)
          {
            setImage3(temp);
            setText3(kind+" "+per+"%");
          }
          else if(i==2)
          {
            setImage4(temp);
            setText4(kind+" "+per+"%");
          }
          else if(i==3)
          {
            setImage5(temp);
            setText5(kind+" "+per+"%");
          }
        }
    });
      alert("서버에 등록이 완료되었습니다!");
    } else {
      alert("사진을 등록하세요!")
    }
  }

  return (
    <div className="uploader-wrapper">
      <input type="file" accept="image/*"
             onChange={saveImage}
        // 클릭할 때 마다 file input의 value를 초기화 하지 않으면 버그가 발생할 수 있다
        // 사진 등록을 두개 띄우고 첫번째에 사진을 올리고 지우고 두번째에 같은 사진을 올리면 그 값이 남아있음!
             onClick={(e) => e.target.value = null}
             ref={refParam => inputRef = refParam}
             style={{display: "none"}}
      />
      <div className="img-wrapper">
        <div className='img-one'>
        <img src={image.preview_URL} />
        <p className='ttext'>이미지를 선택해주세요.!</p>
        </div>
        
      </div>

      <div className="upload-button">
        <Button type="primary" variant="contained" onClick={() => inputRef.click()}>
          Preview
        </Button>
        <Button color="error" variant="contained" onClick={deleteImage}>
          Delete
        </Button>
        <Button color="success" variant="contained" onClick={sendImageToServer}>
          Upload
        </Button>
      </div>
      <div className='img-array'>
        <div className='img-arrays'>
        <img src={image2}/>
        <p className='ttext'>{text2}</p>
        </div>
        <div className='img-arrays'>
        <img src={image3}/>
        <p className='ttext'>{text3}</p>
        </div>
        <div className='img-arrays'>
        <img src={image4}/>
        <p className='ttext'>{text4}</p>
        </div>
        <div className='img-arrays'>
        <img src={image5}/>
        <p className='ttext'>{text5}</p>
        </div>
      </div>
    </div>
  );
}

export default Uploader;