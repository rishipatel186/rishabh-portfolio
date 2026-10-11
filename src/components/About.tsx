import "./styles/About.css";
import { config } from "../config";

const About = () => {
  const highlights = ["React.js", "Node.js", "MongoDB", "MERN Stack", "full-stack"];

  const highlightText = (text: string) => {
    const parts = text.split(new RegExp(`(${highlights.join("|")})`, "g"));
    return parts.map((part, i) =>
      highlights.includes(part)
        ? <mark key={i} className="about-highlight">{part}</mark>
        : part
    );
  };

  return (
    <div className="about-section" id="about">
      <div className="about-me">
        <div className="about-badge">
          <span className="about-badge-dot"></span>
          <span>{config.about.title}</span>
        </div>
        <p className="para">
          {highlightText(config.about.description)}
        </p>
        <div className="about-divider"></div>
        <div className="about-chips">
          {["MERN Stack", "Full-Stack Dev", "AI & Automation", "MCA @ CHARUSAT"].map((chip) => (
            <span key={chip} className="about-chip">{chip}</span>
          ))}
        </div>
      </div>
    </div>
  );
};

export default About;
